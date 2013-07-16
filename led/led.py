#!/usr/bin/env python

# Control a LED attached to GPIO pin 4.
# Like all GPIO activity, requires to be run as root.


import sys
import RPi.GPIO as GPIO

if len(sys.argv) < 2:
  print "usage: led.py on|off"
  sys.exit(1)

switch_on = sys.argv[1] == "on"

# gpio pin to use
IOPIN=4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Our LED is wired to the 3.3v rail and grounded into the
# PI, so HIGH is OFF, LOW is on.

if switch_on:
  mode = GPIO.LOW
else:
  mode = GPIO.HIGH

GPIO.setup(IOPIN, GPIO.OUT, initial=mode)

# GPIO.cleanup()




