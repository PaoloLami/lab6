import RPi.GPIO as GPIO
from LED8x8 import LED8x8
import multiprocessing
import time

col = multiprocessing.Value('i')
col.value = 0b00010000
row = multiprocessing.Value('i')
row.value = 4

dataPin, latchPin, clockPin = 23, 24, 25
disp = LED8x8(dataPin, latchPin, clockPin, row, col)

try:
  while True:
    row.value,col.value = disp.bug(row,col)
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
  disp.p.terminate() 
  disp.p.join(2) 