from datetime import datetime
import json
import os
import subprocess
import time

def main():
    try:
        f = open("activity_dir.txt", "r")
        original_dir = f.read().strip().rstrip("/")
        activity_dir = original_dir + "_unzipped"
        completed_activity_dir = original_dir + "_uploaded"
        if not os.path.exists(completed_activity_dir):
            os.mkdir(completed_activity_dir)
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
        out = out.decode("utf-8")
        if '"id"' in out:
            print("Activity successfully uploaded!")
            os.rename(os.path.join(activity_dir, activity),
                      os.path.join(completed_activity_dir, activity))
        elif "Rate Limit Exceeded" in out:
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
            print("Rate limit reached at " + dt_string + ", waiting 15 minutes")
            time.sleep(900)
            print("Starting up again at " + dt_string)
        else:
            print("Error uploading activity.")

if __name__=='__main__':
    main()

