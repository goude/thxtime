from __future__ import print_function
import json
import os
import time

thxtime_path = os.environ['THXTIME_PATH']
datafile = os.path.join(thxtime_path, 'thxdata.json')
with open(datafile, 'rb') as data_fh:
    data = json.load(data_fh)
    current_time = time.strftime("%H:%M", time.localtime())
    if current_time in data:
        print(data[current_time])
    else:
        print(current_time)

