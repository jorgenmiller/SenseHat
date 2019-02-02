from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear() #clear LED matrix

def get_gyroscope_data():
    gyroscope_data = sense.get_gyroscope_raw() #returns dict of x,y,z
    for item in gyroscope_data:  #cut each to 1 decimal place
        gyroscope_data[item] = round(gyroscope_data[item], 1)
    return gyroscope_data

print("Angular Velocity")
print(["x", "y", "z"])

while True:
    print(get_gyroscope_data())
    time.sleep(.1)
