import sys
import json
import yaml
import sqlite3
import requests
import datetime
from requests.auth import HTTPBasicAuth


def get_techism_id(ext_id):
    cursor.execute('select techism_id from events where ext_id=?', (ext_id,))
    row = cursor.fetchone()
    return row[0] if row else None

def save_event(ext_id, techism_id, event):
    cursor.execute("delete from events where ext_id=?", (ext_id,))
    cursor.execute("insert into events values (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (ext_id,techism_id,event['title'],'',event['url'],event['date_time_begin'],event['date_time_end'],'','','','','',''))

def post(event):
    data = json.dumps(event)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(url, data=data, headers=headers, auth=HTTPBasicAuth(user, password))
    if response.status_code == requests.codes.ok:
        print("Saved event %s" % response.text)
        return response.text
    else:
        print("Error: status code=%s, text=%s" % (response.status_code, response.text))
        return None

def out_of_range(event):
    begin = datetime.datetime.strptime(event["date_time_begin"], "%Y-%m-%d %H:%M")
    today = datetime.datetime.now()
    four_weeks = datetime.timedelta(weeks = 2)
    return begin < today or begin > today + four_weeks

configfile = sys.argv[1]
config = yaml.safe_load(open(configfile))
url = config['url']
db = config['db']
user = config['user']
password = config['password']

conn = sqlite3.connect(db)
cursor = conn.cursor()
cursor.execute('''create table if not exists events
                  (ext_id,techism_id,title,description,url,date_time_begin,date_time_end,tags,
                  loc_name,loc_street,loc_city,loc_latitude,loc_longitue)''')

for line in sys.stdin:
    event = json.loads(line)
    if out_of_range(event):
        print("Skipping event, out of range")
        continue
    ext_id = event['_ext_id']
    techism_id = get_techism_id(ext_id)
    if techism_id:
        event['id'] = techism_id
        # TODO: update event
    else:
        techism_id = post(event)
        save_event(ext_id,techism_id, event)

conn.commit()
conn.close()

