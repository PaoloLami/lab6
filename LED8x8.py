from shifter import Shifter 

pattern1 = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]
pattern = [0b11000011, 0b10111101, 0b01011010, 0b01111110, 0b01011010, 0b01100110, 0b10111101, 0b11000011]

class LED8x8():

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def display(self, num):
    self.shifter.shiftByte(pattern[num])  # load the row values
    self.shifter.shiftByte(1 << (num)) #select current row
  




