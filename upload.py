import json
import os
import subprocess

def main():
    try:
        f = open("activity_dir.txt", "r")
        activity_dir = f.read().strip().rstrip("/") + "_unzipped"
    except IOError:
        print("Please run setup.py and ensure the activity_dir.txt file contains a valid path")
        return

    code = get_code()
    if code == None:
        print("Error parsing URL. Make sure there is a \"code\" field in the URL in url.txt.")
        return

    proc = subprocess.Popen(["curl -X POST https://www.strava.com/oauth/token \
        -F client_id=59592 \
        -F client_secret=1b997bf3f94b3458a646169b3f381f591a5fdf9a \
        -F code=" + code + " \
        -F grant_type=authorization_code"],
        shell=True, stdout=subprocess.PIPE)

    (out, err) = proc.communicate()
    response = json.loads(out.decode("utf-8"))
    if "access_token" in response:
        bearer_token = response["access_token"]
    else:
        print("Error getting permission to upload to Strava. "
              "Visit\nhttps://www.strava.com/oauth/authorize?client_id=59592&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:write,activity:write\n"
              "and copy the URL you are redirected to in url.txt")
        return

    for activity in os.listdir(activity_dir):
        activity_path = os.path.join(activity_dir, activity)
        proc = subprocess.Popen(["curl -X POST https://www.strava.com/api/v3/uploads \
            -H 'Authorization: Bearer " + bearer_token + "' \
            -F activity_type='run' \
            -F data_type='fit' \
            -F external_id='1234825039' \
            -F file=@" + activity_path],
            shell=True, stdout=subprocess.PIPE)

        (out, err) = proc.communicate()
        if '"id"' in out.decode("utf-8"):
            print("Activity successfully uploaded!")
        else:
            print("Error uploading activity.")

def get_code():
    url = ""
    url_file = open("url.txt")
    for line in url_file:
        if line.startswith("http"):
            url = line.strip()
            break
    
    code = None
    args = url.split('&')
    for arg in args:
        if arg.startswith("code="):
            code = arg.split('=')[1]
            break

    return code

if __name__=='__main__':
    main()

