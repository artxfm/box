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
  (wait a long time...)
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

```bash
  $ screen /dev/tty.PL2303-NNNN 115200
```

Screen can be confusing if you haven't used it before. Consult the man
page. But to exit screen you need to type ^A^\ (that's CTRL-A CTRL-\).
