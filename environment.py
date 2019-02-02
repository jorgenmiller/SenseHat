from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

p = round(sense.get_pressure(), 1)
t = round(sense.get_temperature(), 1)
h = round(sense.get_humidity(), 1)

def get_environment_data():
    environment_data = [p, t, h]
    return environment_data

while True:
    print get_environment_data()
    wait = input()
