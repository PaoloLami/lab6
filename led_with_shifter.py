import time
import RPi.GPIO as GPIO
from led_display import LEDdisplay

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 23, 24, 25

theLEDdisplay= LEDdisplay(dataPin, latchPin, clockPin)

try: 
  while True:
    theLEDdisplay.setNumber(1)
except KeyboardInterrupt:
  GPIO.cleanup()
  