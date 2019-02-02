from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

def get_orientation_data():
    orientation = sense.get_orientation_degrees()
    orientation_data = [round(orientation["pitch"], 1), round(orientation["roll"], 1), round(orientation["yaw"], 1)]
    return orientation_data

print(["pitch", "roll", "yaw"])

while True:
    print(get_orientation_data())
    time.sleep(.1)
