import sys
import ical

url = sys.argv[1]
tags = sys.argv[2].split(",")
if len(sys.argv) == 4:
    prefix = ""
    filename = sys.argv[3]
if len(sys.argv) == 5:
    prefix = sys.argv[3]
    filename = sys.argv[4]

ical.process_ical(url, tags, prefix, filename)

