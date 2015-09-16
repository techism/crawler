import os
import sys
from time import sleep
from random import shuffle
import random


def crawl(line):
    cmd1 = "python crawlers/%s > tmp/crawler.result" % line
    print(cmd1)
    os.system(cmd1)
    cmd2 = "cat tmp/crawler.result | python aggregator/aggregator.py aggregator/config.yaml"
    print(cmd2)
    os.system(cmd2)
    sleep(10)

lines = open("crawlers/config").read().splitlines()
shuffle(lines)
for line in lines:
    if line and not line.startswith("#"):
        crawl(line)

