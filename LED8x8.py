from shifter import Shifter 
import time
import RPi.GPIO as GPIO
import multiprocessing
import random


class LED8x8():

  def __init__(self, data, latch, clock, row,col):
    self.shifter = Shifter(data, latch, clock)
    p = multiprocessing.Process(target=self.display, args=(row,col))
    p.daemon = True
    p.start()

  def display(self, row, col):
    #pat[0], pat[1], pat[2], pat[3], pat[4], pat[5], pat[6], pat[7] = 0b11000011, 0b10111101, 0b01011010, 0b01111110, 0b01011010, 0b01100110, 0b10111101, 0b11000011
    pattern = col
    while True:
      self.shifter.shiftByte(pattern)  # load the row values
      self.shifter.shiftByte(1 << (row-1)) #select current row
      time.sleep(0.001)

  def bug(self, row, col):
    while True:
      x = random.randint(-1, 1)
      y = random.randint(-1, 1)
      row += y
      if x == -1:
        col << 1
      elif x == 1:
        col >> 1
      if row < 0: 
        row = 0
      if row > 7:
        row = 7
      return row, col
      time.sleep(0.1)





