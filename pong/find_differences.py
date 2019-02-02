from sense_hat import SenseHat, ACTION_PRESSED
import time
import random

sense = SenseHat()
sense.clear([255, 255, 255])


class Display:
    display = [[255, 0, 255]] * 64

game = Display()


def find_differences():
  display = sense.get_pixels()
  for i in range(64):
    if game.display[i] != display[i]:
      sense.set_pixel(i % 8, int(i / 8), game.display[i]

find_differences()
print(sense.get_pixels())
