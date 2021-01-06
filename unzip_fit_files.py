import gzip
import os
import shutil

def main():
    try:
        f = open("activity_dir.txt", "r")
        activity_dir = f.read().strip()
    except IOError:
        print("Please run setup.py and ensure the activity_dir.txt file contains a valid path")
        return

    unzipped_activity_dir = activity_dir + "_unzipped"
    if not os.path.exists(unzipped_activity_dir):
        os.mkdir(unzipped_activity_dir)

    files = os.listdir(activity_dir)
    fit_files = [fit_file for fit_file in files if fit_file[-7:].lower()=='.fit.gz']
    for fit_file in fit_files:
        unzipped_file = os.path.join(unzipped_activity_dir, fit_file[:-3])
        zipped_file = os.path.join(activity_dir, fit_file)
        if not os.path.exists(unzipped_file):
            with gzip.open(zipped_file, 'rb') as f_in:
                with open(unzipped_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

if __name__=='__main__':
    main()
