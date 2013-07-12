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

You can find all the information you need in
[this guide](http://elinux.org/RPi_Easy_SD_Card_Setup).

If you are on **OSX** and used to mucking about with unix you can do
this:

1. Grab "Raspbian Wheezy" image (zip file) from
[here](http://www.raspberrypi.org/downloads)

2. Insert the SD into the mac, fire up Disk Utility and choose **Verify
Disk** on the SD mount. Note the path (eg, "/dev/disk1s1" or similar).
Then **unmount** the SD volume.

3. Now you need to write the image onto the SD card. You'll need to
unzip the wheezy image you downloaded, then use the dd command. Note
that the output file is the name of the disk **minus the partition
number**. So if you found the original SD volumne was called
"/dev/disk1s1", then the path you want is "/dev/disk1".  CAREFUL! If you
fat finger this you could wipe your computer.

    ```bash
    $ sudo dd if=/path/to/wheezy.img of=/dev/diskN bs=1m
    (...wait a long time...)
    ```

When the dd command is done, you can pull out the SD card and insert it
into the pi.


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

Then you should modify your interfaces config file and turn off the hard
wired internet.

```bash
  $ sudo vi /etc/network/interfaces

  change:
    iface eth0 inet dhcp
  to:
    # iface eth0 inet dhcp

  Also make sure there is an "auto wlan0" line in there.
```

At this point your wlan may come up all by itself. If not try restarting it:

```bash
  $ sudo ifdown wlan0
  $ sudo ifup wlan0
```

### WiFi Reference Links ###

*  http://prupert.wordpress.com/2010/06/25/how-to-configure-wireless-wifi-networking-in-ubuntu-via-the-command-line-cli/
