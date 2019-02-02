from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear() #clear LED matrix

def get_environment_data():
    environment_data = [sense.get_pressure(), sense.get_temperature(), sense.get_humidity()]
    for item in range(len(environment_data)): #cut each to 1 decimal place
        environment_data[item] = round(environment_data[item], 1)
    return environment_data

print(["pressure", "temperature", "humidity"])
print(["millibars", "degrees celsius", "percent of relative humidity"])

while True:
    print get_environment_data()
    time.sleep(.1)
