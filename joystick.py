from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear() #clear LED matrix

while True:
    print(sense.stick.wait_for_event()) #print each event triggered
