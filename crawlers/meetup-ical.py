import sys
import ical

meetup_id = sys.argv[1]
url = "http://www.meetup.com/%s/events/ical/" % meetup_id
tags = sys.argv[2].split(",")
if len(sys.argv) == 4:
    prefix = ""
    filename = sys.argv[3]
if len(sys.argv) == 5:
    prefix = sys.argv[3]
    filename = sys.argv[4]

ical.process_ical(url, tags, prefix, filename)

