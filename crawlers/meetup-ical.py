import sys
from icalendar import Calendar, Event
import json
import yaml
from pytz import timezone as pytz_timezone
import requests
import common

def ical_to_json(event):
    return common.event_as_json(
        ext_id=event.get("uid").encode("utf-8"),
        title=prefix + event.get("summary").encode("utf-8"),
        url=event.get("url").encode("utf-8"),
        date_time_begin=event.get("dtstart").dt,
        date_time_end=event.get("dtend").dt,
        tags=tags)

def process_ical(data):
    cal = Calendar.from_ical(data)
    with open(filename, 'w') as f:
        for vevent in cal.walk("vevent"):
            event = ical_to_json(vevent)
            f.write(event)

meetup_id = sys.argv[1]
url = "http://www.meetup.com/%s/events/ical/" % meetup_id
tags = sys.argv[2].split(",")
if len(sys.argv) == 4:
    prefix = ""
    filename = sys.argv[3]
if len(sys.argv) == 5:
    prefix = sys.argv[3]
    filename = sys.argv[4]


print("Requesting data from %s" % url)
response = requests.get(url)
if response.status_code == requests.codes.ok:
    print("Processing data")
    process_ical(response.text)
else:
    print("Error: status code=%s, text=%s" % (response.status_code, response.text))

