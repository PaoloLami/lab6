from shifter import Shifter 
import time
import multiprocessing
import random

pattern = [
0b10000000, # 0
0b01000000, # 1
0b00100000, # 2
0b00010000, # 3
0b00001000, # 4
0b00000100, # 5
0b00000010, # 6
0b00000001, # 7
]


class LED8x8():


  def __init__(self, data, latch, clock, row,col):
    self.shifter = Shifter(data, latch, clock)
    p = multiprocessing.Process(target=self.display, args=(row,col))
    p.daemon = True
    p.start()

  def display(self, row, col):
    #pat[0], pat[1], pat[2], pat[3], pat[4], pat[5], pat[6], pat[7] = 0b11000011, 0b10111101, 0b01011010, 0b01111110, 0b01011010, 0b01100110, 0b10111101, 0b11000011
    while True:
      self.shifter.shiftByte(pattern[col])  # load the row values
      self.shifter.shiftByte(1 << (row-1)) #select current row
      time.sleep(0.001)

  def bug(self, row, col):
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    row.value += y
    col.value += x
    if col.value < 0: 
      col.value = 0
    if col.value > 7:
      col.value = 7
    if row.value < 0: 
      row.value = 0
    if row.value > 7:
      row.value = 7
    return row.value, col.value
    





