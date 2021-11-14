import time
import RPi.GPIO as GPIO
from shifter import Shifter 


dataPin, latchPin, clockPin = 23, 24, 25
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

class LED8x8():

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def display(self, num):
    self.shifter.shiftByte(pattern[num])  # load the row values
    self.shifter.shiftByte(1 << (num-1)) #select current row
  

try: 
  while True:
    LED = LED8x8(dataPin, latchPin, clockPin)
    for n in range(len(pattern)):
      LED.display(n)
      time.sleep(0.01)
except KeyboardInterrupt:
  GPIO.cleanup()


