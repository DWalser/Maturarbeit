# This assumes pySerial is installed
# Also, this script is highly inefficient. The serial port is 
# opened and closed EVERY time it is updated...but it works. :)

import Blender
from Blender import Mathutils
from math import degrees
import serial

# Create a serial object. The name will need changed accordingly
ser = serial.Serial("COM5")

# Get the object named "Cube".
eul = Blender.Object.Get("Cube").getEuler("worldspace")

# Some offsets may need done
s = 90 - degrees(eul.y)

# Make sure its 1 byte (there might be a better way of insuring this)
data = chr(int(s))

# This is kinda obvious
ser.write(data)

# Close the serial port.
ser.close()
