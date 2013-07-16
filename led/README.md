LED
=============
Script to control the awesome LED.


Hook Up
--------------

We will wire this up so that the RPI is the drain (ground) for the
circuit.  So the LED is connected to the 3.3V rail through a 470 ohm
resistor.  The negative side of the LED connects to the GPIO pin, so
when we set the pin LOW current will flow.

    Cobbler GPIO #4 --> LED cathode (-)
    LED anode (+) --> 470 ohm resistor
    470R --> +3.3V


Software
----------------
See the [simple python code](led.py)
