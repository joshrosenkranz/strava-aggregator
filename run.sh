#!/bin/bash
python3 setup.py $1
python3 unzip_fit_files.py
python3 filter_fit_files.py
python3 upload.py $2