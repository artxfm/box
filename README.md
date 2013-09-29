

box
===

A raspberry pi based streamer [box](https://www.dropbox.com/s/lz5jfjrbqe1v3qf/box-sm.jpg)


Features
--------

1.  Connects to local wifi and streams ARTxFM.
2.  Audio output through 3.5mm stereo jack
3.  Volume control knob.
4.  Standard 2 prong plug for power.
5.  Has LED that lights up when some sort of ARTxFM
    special event is going on.
7.  Periodically checks in with a web service to find out
    if it should update itself or turn on/off its special
    event LED.
8.  Basic web UI that lists all the known
    boxes with their check in history.


Hardware Components
-------------------

1.  Raspberry Pi
2.  SD card
3.  Enclosure
4.  panel mount 3.5mm female stereo jack
5.  ADC chip (eg, MCP3008)
6.  panel mount pot (volume control)
7.  nice knob for the pot
8.  small breadboard for adc and mix wiring
9.  power supply
10.  WiFi module (~$12)
12.  LED for "awesome activity"
13.  misc resistors
14.  wiring


-  [Rough component sketch](https://www.dropbox.com/s/ken41udn5poh1pn/2013-06-24%2011.56.48.jpg)



Get Started!
-------------------

### PI OS ###

Our [Raspberry Pi Setup Guide](rpi-config.md) walks you through setting
up your pi to attach to a wireless network and start streaming ARTxFM!


### Optional code to do cool stuff ###

**"checkin** -- Run periodically to report status and turn LED on/off.
[checkin.py](checkin.py)

**"voulmed"** -- Program to monitor the volume pot and adjust the audio
  output level.  [See VOLD](README_VOLD.md)

**"ledctl"** -- Program that can turn our awesome LED on and
  off. [See LED](README_LED.md)



### Admin/Web Interface ###

The boxes we are building at ARTxFM are designed to checkin with a
server.  

See [boxmaster](https://github.com/artxfm/boxmaster)


