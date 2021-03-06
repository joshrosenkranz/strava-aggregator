# strava-aggregator

Note: These instructions only allow 100 activity uploads per 15 minutes and only 1000 per day.

To upload all of your activities that take place within 20 kilometers of MIT to the shared Strava account:
- Bulk export your Strava activities from your personal Strava account following the instructions [here](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export#Bulk). This may take a couple of hours for Strava to email you and for you to download the data.
- Download this codebase by running `git clone https://github.com/joshrosenkranz/strava-aggregator.git` in your OSX/Linux terminal. If you have Windows, I'm sorry.
- Enter the folder by running `cd strava-aggregator`.
- To unzip, filter, and upload your files:
    - To upload to the women's shared Strava account run `./run.sh /path/to/strava/activities/folder w`
    - To upload to the men's shared Strava account run `./run.sh /path/to/strava/activities/folder m`
    - `/path/to/strava/activities/folder` is the in the Strava export folder that you downloaded in the prior step (for example `~/Downloads/export_15398538/activities`).
