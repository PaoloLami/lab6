from shifter import Shifter 
import time
import RPi.GPIO as GPIO
import multiprocessing

pattern = [0b11000011, 0b10111101, 0b01011010, 0b01111110, 0b01011010, 0b01100110, 0b10111101, 0b11000011]

class LED8x8():

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

  def display(self):
    while True:
      for n in range(8):
        self.shifter.shiftByte(pattern[n])  # load the row values
        self.shifter.shiftByte(1 << (n)) #select current row
        time.sleep(0.001)
    

  p = multiprocessing.Process(target=display)

dataPin, latchPin, clockPin = 23, 24, 25
disp = LED8x8(dataPin, latchPin, clockPin)
try:
  disp.p.daemon = True
  disp.p.start()
except KeyboardInterrupt:
  GPIO.cleanup()
  disp.p.terminate() 
  disp.p.join(2) 




