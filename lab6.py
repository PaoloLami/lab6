import time
import RPi.GPIO as GPIO
import LED8x8 as LED


dataPin, latchPin, clockPin = 23, 24, 25

try: 
  while True:
    disp = LED(dataPin, latchPin, clockPin)
    for n in range(8):
      disp.display(n)
      time.sleep(0.001)
except KeyboardInterrupt:
  GPIO.cleanup()