from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

def get_compass_data():
    compass_data = round(sense.get_compass(), 1)
    return compass_data

print("North")

while True:
    print(get_compass_data())
    time.sleep(.1)
