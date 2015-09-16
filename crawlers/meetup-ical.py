import sys
from icalendar import Calendar, Event
import json
import yaml
from pytz import timezone as pytz_timezone
import requests

def date_time_to_json_string(dt):
    local = dt.astimezone(cet)
    return local.strftime("%Y-%m-%d %H:%M") 

def ical_to_json(event):
    ev = dict()
    ev["_ext_id"] = event.get("uid").encode("utf-8")
    ev["title"] = event.get("summary").encode("utf-8")
    ev["url"] = event.get("url").encode("utf-8")
    ev["date_time_begin"] = date_time_to_json_string(event.get("dtstart").dt)
    ev["date_time_end"] = date_time_to_json_string(event.get("dtend").dt)
    ev["tags"] = tags
    return json.dumps(ev)

def process_ical(data):
    cal = Calendar.from_ical(data)
    with open(filename, 'w') as f:
        for event in cal.walk("vevent"):
            ev = ical_to_json(event)
            f.write(ev)
            f.write("\n")

meetup_id = sys.argv[1]
url = "http://www.meetup.com/%s/events/ical/" % meetup_id
tags = sys.argv[2].split(",")
filename = sys.argv[3]
f = open(sys.argv[3], "w")
cet = pytz_timezone("Europe/Berlin")

print("Requesting data from %s" % url)
response = requests.get(url)
if response.status_code == requests.codes.ok:
    print("Processing data")
    process_ical(response.text)
else:
    print("Error: status code=%s, text=%s" % (response.status_code, response.text))

