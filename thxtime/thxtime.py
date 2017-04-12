from __future__ import print_function
import json
import os
import time
from datetime import datetime


def time_string(t):
    thxtime_path = os.environ['THXTIME_PATH']
    datafile = os.path.join(thxtime_path, 'data/thxdata.json')

    with open(datafile, 'rb') as data_fh:
        data = json.load(data_fh)

    return render_time(t, data)


def render_time(t, data):
    current_time_24 = t.strftime("%H:%M")
    current_time_12 = t.strftime("%I:%M")

    if current_time_24 in data:
        return data[current_time_24]
    elif current_time_12 in data:
        return data[current_time_12]
    else:
        return current_time_24


def thx_time(t):
    return time_string(t)


def thx_time_extended(t):
    time_str = '{} {}'.format(
        datetime.utcnow().strftime('%H:%M'),
        time_string(t)
    )
    return time_str


def main():
    now = datetime.fromtimestamp(time.time()).time()
    print(thx_time_extended(now))


if __name__ == '__main__':
    main()
