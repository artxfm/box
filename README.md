box
===

A raspberry pi based streamer box.


Features
--------

1.  Connects to local wifi and streams ARTxFM.
2.  Connects to local stereo via 3.5mm stereo jack.
3.  Offers volumn control knob.
4.  Has "wall-wart" style connection to electrical outlet.
5.  Has power LED which flashes to indicate internal error.
6.  Has another LED that lights up when some sort of ARTxFM
    special event is going on.
7.  Periodically checks in with a web service to find out
    if it should update itself or turn on/off its special
    event LED.
8.  There will be a basic web UI that lists all the known
    boxes with their check in history.


Hardware Components
-------------------

1.  Raspberry Pi
2.  SD card
3.  Enclosure
4.  panel mount 3.5mm female stereo jack
5.  ADC chip (eg, MCP3008)
6.  panel mount pot (volumn control)
7.  nice knob for the pot
8.  small breadboard for adc and mix wiring
9.  power supply
10.  WiFi module (~$12)
11.  LED for power
12.  LED for "awesome activity"
13.  misc resistors
14.  wiring


-  [Rough component sketch](https://www.dropbox.com/s/ken41udn5poh1pn/2013-06-24%2011.56.48.jpg)

-  [Rough box sketch](https://www.dropbox.com/s/cdnkaj802uwy8il/2013-06-24%2009.50.35.jpg)


Software Components
-------------------

### PI OS ###

Linux OS for the pi (start with Wheezy, if that fails us switch to
ArchLinux).

See our [Raspberry Pi Setup Guide](rpi-config.md)


### Custom code to do cool stuff ###

**"manager"** -- The manager is responsible for communicating with the
cloud mothership.
* Sends periodic checkin messages.
* Responds to checkin responses: _reconnect_ to restart the streamer,
  _update_ to update our code bundle, _led_ to control LED on/off,
  _mute_ to disable streaming.

**"streamer** -- Just a wrapper (maybe not even that) around mpc/mpd to
  stream the audio off our server.

**"voulmed"** -- Program to monitor the volume pot and adjust the audio
  output level.

**"ledctl"** -- Program that can turn our awesome LED on and off.


### Admin/Web Interface ###

Includes a web service for managing checkin messages, and an admin page
we can use to view status of the boxes and also turn on the awesome
LEDs.


### Messages ###

Here are the messages that flow between the box and the cloud using the
checkin mechanism controlled by the "manager". These will run over http
and be json encoded.

```
BOX -> CLOUD
  checkin(led=[on|off], id=<BOX_ID>, swversion=<VERSION>)

  response to checkin is an ACK with zero or more possible
  commands:
    update(file=<NAME>, md5=<MD5>)
    reconnect()
    led(on|off)
    mute()
```
