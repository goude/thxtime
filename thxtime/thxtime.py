from __future__ import print_function
import time
from datetime import datetime as dt


def time_string(t):
    data = {
        "3:14": "π",
        "6:28": "τ",
        "11:06": "Hastings",  # 10:66 = 10:60 + 6 = 11:06
        "11:38": "THX",
        "13:37": "Teel",
        "15:17": "95LUTH",
        "22:27": "Baker St."  # 1B = 27
    }

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

# https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def second_spinner(t):
    symbols = [
        '◷',
        '◶',
        '◵',
        '◴',
    ]
    index = int(translate(t.second, 0, 60, 0, 4))
    return symbols[index]

def thx_time_extended(t):
    time_str = 'W{} {} U{}·{} {}'.format(
        dt.now().isocalendar()[1],
        dt.now().strftime('%m-%d'),
        dt.utcnow().strftime('%H'),
        time_string(t),
        second_spinner(t)
    )
    return time_str


def main():
    now = dt.fromtimestamp(time.time()).time()
    print(thx_time_extended(now))


if __name__ == '__main__':
    main()
