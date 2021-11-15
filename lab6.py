import RPi.GPIO as GPIO
from LED8x8 import LED8x8
import multiprocessing

col = multiprocessing.Value('i')
col.value = 0b00010000
row = 4

dataPin, latchPin, clockPin = 23, 24, 25
disp = LED8x8(dataPin, latchPin, clockPin, row, col)

try:
  while True:
    disp.bug(row,col)
except KeyboardInterrupt:
  GPIO.cleanup()
  disp.p.terminate() 
  disp.p.join(2) 