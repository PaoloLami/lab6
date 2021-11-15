from shifter import Shifter 
import time
import RPi.GPIO as GPIO
import multiprocessing

pattern = multiprocessing.Array('i', 8)
pattern[0], pattern[1], pattern[2], pattern[3], pattern[4], pattern[5], pattern[6], pattern[7] = 0b11000011, 0b10111101, 0b01011010, 0b01111110, 0b01011010, 0b01100110, 0b10111101, 0b11000011

class LED8x8():

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

  def display(self,pattern):
    while True:
      for n in range(8):
        self.shifter.shiftByte(pattern[n])  # load the row values
        self.shifter.shiftByte(1 << (n)) #select current row
        time.sleep(0.001)
    
  p = multiprocessing.Process(target=display,args=(pattern))

dataPin, latchPin, clockPin = 23, 24, 25
disp = LED8x8(dataPin, latchPin, clockPin)
try:
  disp.p.daemon = True
  disp.p.start()
  while True:
    pass
except KeyboardInterrupt:
  GPIO.cleanup()
  disp.p.terminate() 
  disp.p.join(2) 




