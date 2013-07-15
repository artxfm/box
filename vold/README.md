VOLD
=========

Control volume with a pot.

What You Need
-------------------

1.  ADC chip [MCP3008](http://www.adafruit.com/products/856)
2.  cobbler break out [at adafruit](http://www.adafruit.com/products/1105)
3.  10K potentiometer [for example](http://www.adafruit.com/products/562)
4.  wires


Hardware Bits
-------------------

When you connect the cobbler you can still connect your serial cable but
you have to break out the pinds from the cobbler board.  The connection
is:

*  RED -> 5V0
*  BLACK -> GND
*  WHITE -> TXD
*  GREEN -> RXD


Follow the wiring instructions [here](http://learn.adafruit.com/downloads/pdf/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi.pdf)





Software Bits
-------------------

    $ supo apt-get install python-dev
    $ sudo apt-get install python setup-tools
    $ sudo easy_install rpi_gpio

Now install pip.  Here's one way:

    $ curl -O https://pypi.python.org/packages/source/p/pip/pip-1.3.1.tar.gz
    $ tar zxvf pip-1.3.1.tar.gz
    $ cd pip-1.3.1
    $ sudo python setup.py install

Now you have pip:

    $ pip --help

I had all kinds of trouble resolving hostnames on my rpi. Not sure if
this is a local DNS issue with the ISP here or what. But I switched my
dns by editing /etc/resolve.conf and setting:

    nameserver 8.8.8.8

 Copy over the `vol.py` code from this repo.  You run this on the pi
 like so:

    $ sudo python vol.py


 Then turn your knob and be amazed!



#### References ####
*  http://learn.adafruit.com/downloads/pdf/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi.pdf
*  https://gist.github.com/ladyada/3151375/raw/035f4344a284b3c5a1c9c8ecbda0a2a8df689198/adafruit_mcp3008.py
*  https://github.com/Mic92/python-mpd2
