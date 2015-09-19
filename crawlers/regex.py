import sys
import yaml
import re
import requests
import common
from datetime import datetime

def build_event(match):
    d = config.copy()
    d.update(match.groupdict())
    dt = common.dict_to_date_time(d)
    return common.event_as_json(
        ext_id='%s@%s' % (dt.strftime('%Y%m%d'),d['url']),
        title=d['title'],
        url=d['url'],
        date_time_begin=dt,
        tags=d['tags']
    )

configfile = sys.argv[1]
config = yaml.safe_load(open(sys.argv[1]))
url = config['url']
regex = config['regex']
p=re.compile(regex)

print("Requesting data from %s" % url)
response = requests.get(url, verify=False)
if response.status_code == requests.codes.ok:
    print("Processing data")
    f = open(sys.argv[2], "w")
    matches=p.finditer(response.text)
    for match in matches:
        event = build_event(match)
        f.write(event)
    f.close()
else:
    print("Error: status code=%s, text=%s" % (response.status_code, response.text))




