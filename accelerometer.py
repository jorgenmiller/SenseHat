from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear() #clear LED matrix

def get_acceleration_data():
    acceleration_data = sense.get_accelerometer_raw() #returns dict of x,y,z linear acceleration
    for item in acceleration_data:  #cut each to 1 decimal place
        acceleration_data[item] = round(acceleration_data[item], 1)
    return acceleration_data

print("Linear Acceleration")
print(["x", "y", "z"])

while True:
    print(get_acceleration_data())
    time.sleep(.1)
