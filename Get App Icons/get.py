#!/usr/bin/env python
#coding=utf-8
#
# Travis
# Copyright 2012 Plumn LLC.

import urllib,os,json



def getIcons(appid='578553766'):
    output='~/Desktop/'
    folder=os.path.expanduser(output+appid+'/')
    
    if not os.path.exists(folder):
        os.mkdir(folder)

    app=json.loads(urllib.urlopen('http://itunes.apple.com/lookup?id='+appid).read())['results'][0]

    name=app['artistName']

    icon512=app['artworkUrl512']

    icon175=icon512.split(".png")[0]+'.175x175-75.png'

    output = open(folder+'512.png','wb')
    output.write(urllib.urlopen(icon512).read())
    output.close()

    output = open(folder+'175.png','wb')
    output.write(urllib.urlopen(icon175).read())
    output.close()

    return app['trackId']