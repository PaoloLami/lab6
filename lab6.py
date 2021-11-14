import time
import RPi.GPIO as GPIO
from LED8x8 import LED8x8


dataPin, latchPin, clockPin = 23, 24, 25
disp = LED8x8(dataPin, latchPin, clockPin)

try: 
  while True:
    for n in range(8):
      disp.display(n)
      time.sleep(0.001)
except KeyboardInterrupt:
  GPIO.cleanup()