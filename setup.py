import os
import subprocess
import sys

def main():
    try:
        import fitparse
    except ImportError:
        subprocess.call("sudo pip2 install -e git+https://github.com/dtcooper/python-fitparse#egg=python-fitparse", shell=True)
        subprocess.call("sudo pip3 install -e git+https://github.com/dtcooper/python-fitparse#egg=python-fitparse", shell=True)

    valid_path_provided = False
    while not valid_path_provided:
        if len(sys.argv) == 2:
            user_input = sys.argv[1]
        else:
            user_input = input("Please enter the path to the Strava activities folder (i.e. ~/Downloads/export_*/activities): ")
        valid_path_provided = check_activity_dir(user_input)

def check_activity_dir(user_input):
    activity_dir = os.path.expanduser(user_input)
    if (os.path.exists(activity_dir)):
        f = open("activity_dir.txt", "w+")
        f.write(activity_dir + "\n")
        f.close()
        valid_path_provided = True
        print("Activity folder set to", activity_dir)
        return True
    else:
        print("Folder", activity_dir, "was not found")
        return False

if __name__=='__main__':
    try:
        input = raw_input
    except NameError:
        pass
    main()