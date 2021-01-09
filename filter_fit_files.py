import fitparse
import os

mit_lat = 42.35785
mit_lon = -71.09708
dist_threshold_km = 20

def main():
    activities_in_boston = []
    try:
        f = open("activity_dir.txt", "r")
        activity_dir = f.read().strip().rstrip("/") + "_unzipped"
    except IOError:
        print("Please run setup.py and ensure the activity_dir.txt file contains a valid path")
        return

    files = os.listdir(activity_dir)
    fit_files = [activity for activity in files if activity[-4:].lower()=='.fit']
    num_fit_files = len(fit_files)
    num_files_parsed = 0
    for activity in fit_files:
        fraction_complete = num_files_parsed * 1.0 / num_fit_files
        fraction_complete = round(fraction_complete * 100)
        if num_files_parsed % 10 == 0:
            print("Finished parsing " + str(fraction_complete) + "% of files")
        activity_file = os.path.join(activity_dir, activity)
        fitfile = fitparse.FitFile(activity_file,  
            data_processor=fitparse.StandardUnitsDataProcessor())
        
        first_gps_point_found = False
        in_boston = False
        messages = fitfile.messages
        for m in messages:
            if not hasattr(m, 'fields'):
                continue
            fields = m.fields
            lat = None
            lon = None
            for field in fields:
                if field.name == "position_lat":
                    lat = field.value
                elif field.name == "position_long":
                    lon = field.value
            if lat and lon:
                dist_to_mit_km = haversine(mit_lat, mit_lon, lat, lon)
                if dist_to_mit_km < dist_threshold_km:
                    in_boston = True
                break

        if in_boston:
            print("Keeping", activity_file)
        else:
            print("Removing", activity_file)
            os.remove(activity_file)

        num_files_parsed += 1

def haversine(lat1, lon1, lat2, lon2):
    from math import sin, cos, sqrt, atan2, radians

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # approximate radius of earth in km
    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

if __name__=='__main__':
    main()
