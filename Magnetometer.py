from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear() #clear LED matrix

def get_compass_data():
    compass_data = round(sense.get_compass(), 1) #returns float 0-360, round to 1 decimal place
    return compass_data

print("Magnetometer")

while True:
    print(get_compass_data())
    time.sleep(.1)
