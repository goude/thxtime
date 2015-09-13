from __future__ import print_function
import json
import os
import time
from datetime import datetime

def get_time_string(t):
    thxtime_path = os.environ['THXTIME_PATH']
    datafile = os.path.join(thxtime_path, 'data/thxdata.json')

    with open(datafile, 'rb') as data_fh:
        data = json.load(data_fh)
        current_time_24 = t.strftime("%H:%M")
        current_time_12 = t.strftime("%I:%M")
        if current_time_24 in data:
            return data[current_time_24]
        elif current_time_12 in data:
            return data[current_time_12]
        else:
            return current_time_24

def main():
    now = datetime.fromtimestamp(time.time()).time()
    print(get_time_string(now))

if __name__ == '__main__':
    main()

