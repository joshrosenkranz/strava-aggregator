import os
import subprocess

try:
    import fitparse
except ImportError:
    subprocess.call("sudo pip2 install -e git+https://github.com/dtcooper/python-fitparse#egg=python-fitparse", shell=True)
    subprocess.call("sudo pip3 install -e git+https://github.com/dtcooper/python-fitparse#egg=python-fitparse", shell=True)

try:
    input = raw_input
except NameError:
    pass
valid_path_provided = False
while not valid_path_provided:
    user_input = input("Please enter the path to the Strava activities folder (i.e. ~/Downloads/export_*/activities): ")
    activity_dir = os.path.expanduser(user_input)
    if (os.path.exists(activity_dir)):
        f = open("activity_dir.txt", "w+")
        f.write(activity_dir + "\n")
        f.close()
        valid_path_provided = True
        print("Activity folder set to", activity_dir)
    else:
        print("Folder", activity_dir, "was not found")