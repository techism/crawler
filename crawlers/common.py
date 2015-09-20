# -*- coding: utf-8 -*-

import json
from pytz import timezone as pytz_timezone
from datetime import datetime,timedelta

cet = pytz_timezone("Europe/Berlin")

month_names = {
    u'Januar':1,
    u'January':1,
    u'Februar':2,
    u'February':2,
    u'März':3,
    u'March':3,
    u'April':4,
    u'Mai':5,
    u'May':5,
    u'Juni':6,
    u'June':6,
    u'Juli':7,
    u'July':7,
    u'August':8,
    u'September':9,
    u'Oktober':10,
    u'October':10,
    u'November':11,
    u'Dezember':12,
    u'December':12,
}

def month_name_to_num(month):
    return month_names.get(month, month)

def dict_to_date_time(d):
    year = int(d['year'])
    month = int(month_name_to_num(d['month']))
    day = int(d['day'])
    hour = int(d['hour'])
    minute = int(d['minute'])
    return datetime(year, month, day, hour, minute, 0, 0, cet)

def date_time_to_json_string(dt):
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


