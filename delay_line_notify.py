# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import os,sys
import ConfigParser

inifile = ConfigParser.SafeConfigParser()
inifile.read('./config.ini')

# LineNotifyへPost
def post_notify(line):
    notify_url = inifile.get('settings','notify_url')
    message = line+"は現在遅延しています。"
    token = inifile.get('settings','token')
    
    params = {"message":message}
    params = urllib.urlencode(params)
    
    req = urllib2.Request(notify_url)
    req.add_header("Authorization","Bearer " + token)
    req.add_data(params)

    res = urllib2.urlopen(req)
    r = res.read()
    print(r)

# 遅延情報取得
delayapi_url = inifile.get('settings','delayapi_url')
r = urllib2.urlopen(delayapi_url)
datas = json.loads(r.read())

line = inifile.get('settings','line')

for data in datas:
    if data["name"] == unicode(line,'utf-8'):
        post_notify(line)
