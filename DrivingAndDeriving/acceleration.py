from sense_hat import SenseHat
import time

print("Driving and Deriving")

sense = SenseHat() #simplify calls to the Hat
sense.clear() #clear LED matrix

year    =   time.strftime( %Y, time.localtime() )
month   =   time.strftime( %m, time.localtime() )
day     =   time.strftime( %d, time.localtime() )
hour    =   time.strftime( %H, time.localtime() )
minute  =   time.strftime( %M, time.localtime() )
second  =   time.strftime( %S, time.localtime() )

data_name = "DrivingAndDerivingData" + "_" + year + "-" + month + "-" + day + "_" + hour + ":" + minute + ":" + second + ".txt"
print(data_name)
data = open(data_name, "a")

def get_acceleration_data():
    acceleration_data = sense.get_accelerometer_raw() #returns dict of x,y,z linear acceleration
#    for item in acceleration_data:  #cut each to 4 decimal places
#        acceleration_data[item] = round(acceleration_data[item], 4)
    return acceleration_data

try:
    while True:
        data.write(get_acceleration_data()['x'])
        time.sleep(.01)

finally:
    sense.clear()
    data.close()
