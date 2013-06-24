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

1.  Linux OS for the pi (start with Wheezy, if that fails us
    switch to ArchLinux).
2.  Program that runs on the pi and kicks off streaming and adjusts
    volume.
3.  Program that runs on the pi and manages configuration, periodic
    checkin, and update. When the pi starts up it will connect somwhere
    to get its configuration.  The only configuration it requires is the
    URI for the stream.
4.  Basic web service for managing checkin messages running in the
    cloud.
5.  Basic web admin interface for displaying box info and also for
    turning on/off the awesome LEDs.  Initially, configuration and
    update will be manual operations.
