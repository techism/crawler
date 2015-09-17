import json
from pytz import timezone as pytz_timezone
from datetime import timedelta

def date_time_to_json_string(dt):
    cet = pytz_timezone("Europe/Berlin")
    local = dt.astimezone(cet)
    return local.strftime("%Y-%m-%d %H:%M") 

def event_as_json(ext_id=None,
          title=None,
          url=None,
          date_time_begin=None,
          date_time_end=None,
          tags=None):
    ev = dict()
    ev["_ext_id"] = ext_id
    ev["title"] = title
    ev["url"] = url
    ev["date_time_begin"] = date_time_to_json_string(date_time_begin)
    if not date_time_end:
        date_time_end = date_time_begin + timedelta(hours=3)
    ev["date_time_end"] = date_time_to_json_string(date_time_end)
    ev["tags"] = tags 
    return json.dumps(ev) + "\n"


