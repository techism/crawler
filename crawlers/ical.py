from icalendar import Calendar, Event
import requests
import common

def ical_to_json(event, tags, prefix):
    return common.event_as_json(
        ext_id=event.get("uid").encode("utf-8"),
        title=prefix + event.get("summary").encode("utf-8"),
        url=event.get("url").encode("utf-8"),
        date_time_begin=event.get("dtstart").dt,
        date_time_end=event.get("dtend").dt,
        tags=tags)

def process_ical(url, tags, prefix, filename):
    print("Requesting data from %s" % url)
    response = requests.get(url, headers={'User-Agent':'Mozilla'})
    if response.status_code == requests.codes.ok:
        print("Processing data")
        cal = Calendar.from_ical(response.text)
        with open(filename, 'w') as f:
            for vevent in cal.walk("vevent"):
                event = ical_to_json(vevent, tags, prefix)
                f.write(event)
    else:
        print("Error: status code=%s, text=%s" % (response.status_code, response.text))

