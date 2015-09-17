import feedparser
import common
import arrow
import sys

f = open(sys.argv[1], "w")
d = feedparser.parse("http://www.munichdot.net/events/feed")
for entry in d.entries:
    dtbegin = arrow.get(entry.updated).datetime
    event = common.event_as_json(
        ext_id=entry.id,
        title=".NET User Group: " + entry.title,
        url=entry.link,
        date_time_begin=dtbegin,
        tags=[".net"])
    f.write(event)
f.close()

