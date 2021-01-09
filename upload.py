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

    proc = subprocess.Popen(["curl ec2-13-59-238-205.us-east-2.compute.amazonaws.com:80"],
                            shell=True, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    bearer_token = out.decode("utf-8").strip()

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

if __name__=='__main__':
    main()

