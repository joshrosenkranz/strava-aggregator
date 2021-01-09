# strava-aggregator

Note: These instructions only allow 100 activity uploads per 15 minutes and only 1000 per day.

To upload all of your activities that take place within 20 kilometers of MIT to the shared Strava account:
- Bulk export your Strava activities from your personal Strava account following the instructions [here](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export#Bulk). This may take a couple of hours for Strava to email you and for you to download the data.
- Run `python setup.py` and enter the path to the `activities` folder in the Strava export folder that you downloaded in the prior step (for example `~/Downloads/export_15398538/activities`).
- Run `python unzip_fit_files.py`.
- Run `python filter_fit_files.py`. This should remove all the activities that do not take place within 20 km of MIT.
- To upload your activities, run `python upload.py`. This should print out "Activity successfully uploaded!" as the activities are uploaded to the shared Strava account.
- Thanks!