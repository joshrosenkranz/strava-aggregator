# strava-aggregator

To upload all of your activities that take place within 20 kilometers of MIT to the shared Strava account:
- Run `python setup.py` and enter the path to the Strava export activities folder.
- Run `python unzip_fit_files.py`.
- Run `python filter_fit_files.py`. This should remove all the activities that do not take place within 20 km of MIT.
- To upload data, visit [this link](https://www.strava.com/oauth/authorize?client_id=59592&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:write,activity:write), authorize the Strava API to gain access to the shared Strava account, and copy the URL you are redirected to in `url.txt`.  (Note: You should replace all the text in `url.txt` with the URL you are redirected to.)
- Then run `python upload.py`. This should print out "Activity successfully uploaded!" as the activities are uploaded to the shared Strava account.
- Thanks!