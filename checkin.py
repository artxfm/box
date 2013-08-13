#!/usr/bin/env python

# Must be run as root.
# sorry horrible hack -- proof of concept!

import urllib2
import json
import time
import subprocess
from mpd import MPDClient
import RPi.GPIO as GPIO
from datetime import timedelta
from datetime import datetime as dt
import sys


def get_uptime():
  with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_string = str(timedelta(seconds = uptime_seconds))
  return uptime_string

def get_box_id():
  # TODO
  return '12345'

def is_muted():
  # TODO
  return False

def get_iwstats():
  o = subprocess.check_output(['iwconfig', 'wlan0'])
  return filter(lambda t:len(t)>2, o.replace("\n", "").split("  "))

def get_ifconfig():
  o = subprocess.check_output(['ifconfig', 'wlan0'])
  return filter(lambda t:len(t)>2, o.replace("\n", "").split("  "))



# init gpio
LEDPIN=4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEDPIN, GPIO.OUT)

# init mpc
client = MPDClient()
client.timeout = 2
client.idletimeout = None
client.connect('localhost', 6600)

# check led
led_state = GPIO.input(LEDPIN)

# get mpd stats
stats = client.status()
stat = client.stats()
client.close()
client.disconnect()

#print "LED = %s" % led_state
#print "MPD_status = %s" % stats
#print "MPD_stats  = %s" % stat
#print "uptime = %s" % get_uptime()
#print "timestamp = %s" % dt.utcnow().isoformat()
 
msg = {"led":(led_state == 0),
       "mpd":{ 
         "status":stats,
         "stat":stat
       },
       "uptime":get_uptime(),
       "timestamp":dt.utcnow().isoformat(),
       "id":get_box_id(),
       "mute":is_muted(),
       "net":{
         "iwconfig":get_iwstats(),
         "ifconfig":get_ifconfig()
       }}

if len(sys.argv) < 2:
  print json.dumps(msg, indent=4)
else:
  url = sys.argv[1]
  payload = json.dumps(msg)
  print "sending to %s" % url
  req = urllib2.Request(url, payload, {'Content-type':'application/json'})
  f = urllib2.urlopen(req)
  response = f.read()
  f.close()
  reply = json.loads(response)

  if reply.has_key('led'):
	onoff='off'
        if reply['led'] == 'on':
		onoff = 'on'
	subprocess.call(["python", "led.py", onoff])




