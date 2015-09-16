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
    ev["_ext_id"] = str(event.get("uid"))
    ev["title"] = str(event.get("summary"))
    ev["url"] = str(event.get("url"))
    ev["date_time_begin"] = date_time_to_json_string(event.get("dtstart").dt)
    ev["date_time_end"] = date_time_to_json_string(event.get("dtend").dt)
    ev["tags"] = tags
    return json.dumps(ev)

meetup_id = sys.argv[1]
url = "http://www.meetup.com/%s/events/ical/" % meetup_id
tags = sys.argv[2].split(",")
cet = pytz_timezone("Europe/Berlin")

data = requests.get(url).text
cal = Calendar.from_ical(data)
for event in cal.walk("vevent"):
    ev = ical_to_json(event)
    print(ev)

