# strava-aggregator

Note: These instructions only allow 100 activity uploads per 15 minutes and only 1000 per day.

To upload all of your activities that take place within 20 kilometers of MIT to the shared Strava account:
- Login to the MIT XC account
    - Email: jp.rosenkranz@comcast.net
    - Password: MITMITMIT
- Run `python setup.py` and enter the path to the Strava export activities folder.
- Run `python unzip_fit_files.py`.
- Run `python filter_fit_files.py`. This should remove all the activities that do not take place within 20 km of MIT.
- To get authorization to upload your activities to the shared Strava account,
    - Make sure you are logged into the shared Strava account. Otherwise this will upload all your runs to your own Strava account.
    - Visit [this link](https://www.strava.com/oauth/authorize?client_id=59592&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:write,activity:write).
    - Authorize the Strava API to gain access to the shared Strava account.
    - Copy the URL you are redirected to in `url.txt`.  (Note: You should replace all the text in `url.txt` with the URL you are redirected to.)
- To upload your activities, run `python upload.py`. This should print out "Activity successfully uploaded!" as the activities are uploaded to the shared Strava account.
- Thanks!