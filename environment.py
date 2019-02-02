from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

def get_environment_data():
    environment_data = [round(sense.get_pressure(), 1), round(sense.get_temperature(), 1), round(sense.get_humidity(), 1)]
    return environment_data

print(["pressure", "temperature", "humidity"])

while True:
    print get_environment_data()
    time.sleep(.1)
