# SenseHat
Adafruit's [Raspberry Pi Sense HAT](https://www.adafruit.com/product/2738)  

[Sense HAT documentation](https://www.raspberrypi.org/documentation/hardware/sense-hat/README.md)  


## Install Library
```
sudo apt-get install sense-hat
```
placed at `/usr/src/sense-hat`

## Calibration
Required for magnetometer, but optional for accelerometer
```
sudo apt-get update
sudo apt-get install octave -y
cd
cp /usr/share/librtimulib-utils/RTEllipsoidFit ./ -a
cd RTEllipsoidFit
RTIMULibCal
```

Remove the original and implement the new calibration

```
rm ~/.config/sense_hat/RTIMULib.ini
sudo cp ~/RTEllipsoidFit/RTIMULib.ini /etc
```

## Usage in Python

[Full Docs](https://pythonhosted.org/sense-hat/)

```python
from sense_hat import SenseHat
sense = SenseHat()
```
