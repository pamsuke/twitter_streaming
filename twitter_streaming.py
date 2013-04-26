#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import tweepy
import commands
  
class StreamListener(tweepy.StreamListener):
    def on_data(self, data):
        if data.startswith("{"):
            print data
        if data.find("disconnected") > -1:
            commands.getoutput("echo disconnected")
            commands.getoutput("date")
  
username = ""
password = ""
# , separated OR search
keyword = "word1,word2,word3"
auth = tweepy.auth.BasicAuthHandler(username, password)
stream = tweepy.Stream(auth, StreamListener())
#stream.sample()
stream.filter(track=[keyword])
