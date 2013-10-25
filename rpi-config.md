Raspberry Pi Configuration
==========================

This describes how to setup your Raspberry Pi for audio streaming.
Warning! This is a work in progress.


Things You'll Need
------------------

* Raspberry Pi - Try the [Model B from Adafruit](http://www.adafruit.com/products/998)
* [Console cable](http://www.adafruit.com/products/954)
* [5V power supply](http://www.adafruit.com/products/501) - Note this
  does not come with a USB cable.
* [4G memory card](http://www.adafruit.com/products/102) - Larger is fine!
* [WiFi module](http://www.adafruit.com/products/814)



Install OS
----------

### Raspbian vs Noobs ###

This guide assumes you are installing the Raspbain "wheezy" image. There
is a new NOOBS image that claims to offer a relatively painless install.
Feel free to use that, then com back here once you have the system
running and fill in the bits you need.  Note that NOOBs install requires
that you hook the pi up to a monitor.

### Installing WHEEZY ###

You can find all the information you need in
[this guide](http://elinux.org/RPi_Easy_SD_Card_Setup).

If you are on **OSX** and used to mucking about with unix you can do
this:

1. Grab "Raspbian Wheezy" image (zip file) from
[here](http://www.raspberrypi.org/downloads)

2. Insert the SD into the mac, fire up Disk Utility and choose **Verify
Disk** on the SD mount. Note the path (eg, "/dev/disk1s1" or similar).
Then **unmount** the SD volume.  Alternatively, you can use command
line, `diskutil list`, then to unmount: `diskutil unmountDisk
/dev/disk3`

3. Now you need to write the image onto the SD card. You'll need to
unzip the wheezy image you downloaded, then use the dd command. Note
that the output file is the name of the disk **minus the partition
number**. So if you found the original SD volumne was called
"/dev/diskr3s1", then the path you want is "/dev/rdisk3".  CAREFUL! If you
fat finger this you could wipe your computer.

Let's assume you are using /dev/disk3, then:

```bash
$ sudo dd if=/path/to/wheezy.img of=/dev/rdisk3 bs=1m
(...wait a bit...)
```

When the dd command is done, you can should eject the disk:

```bash
$ diskutil eject /dev/disk3
```

Pull out the SD card and insert it into the pi.


Serial Communication
--------------------

On OSX, in order to talk to the pi with the adafruit cable you need to
install the pl2303 driver.  Follow the instructions here:
*  http://www.xbsd.nl/2011/07/pl2303-serial-usb-on-osx-lion.html

or if you want to try just using an installer, try this:
*  http://changux.co/osx-installer-to-pl2303-serial-usb-on-osx-lio/


Once you have the extension installed you will have a new tty when you
plug in the cable. For me the path was:

    /dev/tty.PL2303-00001014

To talk to the pi, first connect the cable correctly (see adafruit
product description, or [this](http://learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-5-using-a-console-cable.pdf).

Then, in a terminal fire up screen like so:

    $ screen /dev/tty.PL2303-NNNN 115200


Screen can be confusing if you haven't used it before. Consult the man
page. But to exit screen you need to type ^A^\ (that's CTRL-A CTRL-\\).


Log into your Pi
----------------
Before connecting to the pi, plug in the WiFi module. Then connect
(which applys power) and the Pi will boot up.

When you connect to the Pi over the serial cable, you will eventually
get a login prompt. The default login is:
*  **username**: pi
*  **password**: raspberry

Removing power (ie, unplugging the usb cable) will turn the pi off. To
do that safely you should halt the system first:

    $ sudo /sbin/shutdown -h now

When you see the "Power down" message it is safe to remove power.


Initial Configuration
---------------------
Important things to do are
*  Expand the root FS so that you can use your entire SD card.
*  Set timezone: `sudo dpkg-reconfigure tzdata`

As soon as you log in try:

    $ raspi-config


Security
---------------
The pi will have ssh enabled by default. Good idea to create a new
account and set things up so that only that account can ssh in.

1. Create account with `sudo adduser <NAME>`
2. Add account name to sudo group (edit /etc/group)
3. Edit `/etc/ssh/sshd_config`, add the line `AllowUsers NAME` to the
   end.

Also you should generate new hostkeys:

```bash
  $ sudo rm /etc/ssh/ssh_host_* && sudo dpkg-reconfigure openssh-server
```



WiFi
----------------
The WiFi module should be recognized by the OS. Check the status:
*  `iwstatus` Gets the status of the interface
*  `iwlist scan` Will show various wifi networks about

Now I assume you want to connect to your WPA2 protected network. If you
want to do something else then search interwebs for how to setup
wpa_supplicant on ubuntu for your situation.

Create passphrase config block:

     $ wpa_passpharse SSID PASSWORD

That will output something like:

```bash
  network={
        ssid="SSID"
        #psk="PASSWORD"
        psk=9e7b404c12324288d37f0ad27cfdafa275d1320ae8e700a92541d5d67998e365
  }
```

Now you need to create config file for wpa_supplicant.  The config file
is here:

    /etc/wpa_supplicant/wpa_supplicant.conf

Make yours look something like the example below. In that example, the
SSID is "frogger":

```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
  ssid="frogger"
  scan_ssid=1
  proto=RSN
  pairwise=CCMP TKIP
  key_mgmt=WPA-PSK
  psk=9e7b404c1fc84288d37f0ad2712345a275d1320ae8e700a92541d5d67998e365
}
```

Then you should modify your interfaces config file.  
Edit `/etc/network/interfaces`:

```bash
auto lo

iface lo inet loopback
# iface eth0 inet dhcp

allow-hotplug wlan0
auto wlan0
# iface wlan0 inet dhcp
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf

iface default inet dhcp
```

Note that I commented out the eth0 (wired) connection.
At this point your wlan may come up all by itself. If not try restarting it:

```bash
  $ sudo ifdown wlan0
  $ sudo ifup wlan0
```

It will take a few seconds for the wifi to connect.


### Open Wifi Network

If you have an open wifi network, then you can connect by simply doing
this:

```bash
  $ sudo iwconfig wlan0 essid NETWORK_ID
  $ sudo dhclient wlan0
```



#### WiFi Reference Links ####

*  http://prupert.wordpress.com/2010/06/25/how-to-configure-wireless-wifi-networking-in-ubuntu-via-the-command-line-cli/
*  http://www.raspberrypi.org/phpBB3/viewtopic.php?t=6256&p=188783
*  http://www.raspberrypi.org/phpBB3/viewtopic.php?t=11517


Software Configuration
----------------------

First upgrade your pi:
```bash
  $ sudo apt-get update
  $ sudo apt-get upgrade
```

Because plain old vi can be improved:

    $ sudo apt-get install vim

Then reboot and make sure everything is still working properly:

    $ sudo shutdown -r now

Get audio system working:

```bash
  $ sudo apt-get install mpg321
  $ sudo apt-get install lame
  $ sudo modprobe snd-bcm2835
  $ sudo amixer cset numid=3 1
```

Test your audio.  Plug in to the analog audio out, then:

    $ aplay /usr/share/sounds/alsa/Rear_Center.wav


Now configure MPC for streaming

```bash
  sudo apt-get install mpd mpc
```

At the end of the install you may get a bind error.  Just ignore it.

Then follow the
[guide](http://cagewebdev.com/index.php/raspberry-pi-playing-internet-radio/)
to set the proper permissions, alter the config file, and then reboot
your pi.

When the pi comes back up try this:

```bash
$ mpc add http://s7.viastreaming.net:8310/
$ mpc play
```

Example of adjusting the volume with mpc:

    $ mpc volume -10

To set the box up to start streaming at boot, edit /etc/init.d/mpc and
add a line to the "start" function that kicks off the mpc.  The line
to add is:

    /usr/bin/mpc play



#### Reference for Software ####
*  http://cagewebdev.com/index.php/raspberry-pi-getting-audio-working/
*  http://cagewebdev.com/index.php/raspberry-pi-playing-internet-radio/



### Python Extras ###

You will want this if you want to install the boxmaster checkin tool.

```bash
$ sudo apt-get install python-dev python-setuptools
```



Next Steps
--------------------
*  To add a potentiometer so that you can control volume with a knob, see
   [the vold readme](vold/README.md)
*  To add the awesome LED, see [the led readme](led/README.md)

