from shifter import Shifter 
import time
import multiprocessing
import random

pattern = [
0b01111111, # 0
0b10111111, # 1
0b11011111, # 2
0b11101111, # 3
0b11110111, # 4
0b11111011, # 5
0b11111101, # 6
0b11111110, # 7
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
      self.shifter.shiftByte(pattern[col.value])  # load the row values
      self.shifter.shiftByte(1 << (row.value)) #select current row
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
    





