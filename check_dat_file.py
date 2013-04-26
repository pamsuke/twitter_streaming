#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from datetime import datetime
from datetime import timedelta

fname = raw_input("Enter dat filename: ")

lines = open(fname, "r")

tweets = []
for line in lines:
    try:
        tweet = json.loads(line)
        if tweet.has_key("created_at"):
          tweets.append(tweet)
    except:
        pass

print "\n\n" + fname + " has " + str(len(tweets)) + " tweets.\n\n" 

print "from:"
print datetime.strptime(tweets[0]["created_at"], '%a %b %d %H:%M:%S +0000 %Y') + timedelta(hours=9)
print "To:"
print datetime.strptime(tweets[-1]["created_at"], '%a %b %d %H:%M:%S +0000 %Y') + timedelta(hours=9)
print "\n\n"

count = int(raw_input("What is tweets list index?: "))

for tw in tweets[:count]:
	print datetime.strptime(tw["created_at"], '%a %b %d %H:%M:%S +0000 %Y') + timedelta(hours=9)

