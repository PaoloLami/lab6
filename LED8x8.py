from shifter import Shifter 
import time
import RPi.GPIO as GPIO
import multiprocessing

pat = multiprocessing.Array('i', 8)

class LED8x8():

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
    p = multiprocessing.Process(target=self.display)
    p.daemon = True
    #p.start()

  def display(self):
    pat[0], pat[1], pat[2], pat[3], pat[4], pat[5], pat[6], pat[7] = 0b11000011, 0b10111101, 0b01011010, 0b01111110, 0b01011010, 0b01100110, 0b10111101, 0b11000011
    while True:
      for n in range(8):
        self.shifter.shiftByte(pat[n])  # load the row values
        self.shifter.shiftByte(1 << (n)) #select current row
        time.sleep(0.001)

dataPin, latchPin, clockPin = 23, 24, 25
disp = LED8x8(dataPin, latchPin, clockPin)

try:
  disp.display()
except KeyboardInterrupt:
  GPIO.cleanup()
  disp.p.terminate() 
  disp.p.join(2) 




