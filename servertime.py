# MIT License, by Aftermoon / https://github.com/Aftermoon-dev

import urllib.request
import datetime
import maya

def getTargetTimeZone():
    try:
        file = open('timezone.ini', 'r')
    except IOError:
        print("Can't open timezone.ini, Using GMT.")
        return 'GMT'

    timezone = file.readline()
    if timezone != '':
        print("TimeZone : {}".format(timezone))
        return timezone
    else:
        print("timezone.ini is Empty, Using GMT.")
        return 'GMT'
    file.close()
def getServerTime(server):
    return urllib.request.urlopen(server).headers['Date']
def cvtTimezone(date):
    cvtDate = maya.parse(date).datetime(to_timezone=getTargetTimeZone())
    return cvtDate.replace(tzinfo=None)

targetServer = input("Enter a Webpage Address (ex. http://google.com/) : ")
serverTime = getServerTime(targetServer)
cvtServerTime = cvtTimezone(serverTime)
print('Server Time : {}'.format(cvtServerTime))



