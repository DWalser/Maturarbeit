import sys
import bpy
sys.path.append("/Users/nicole/Repositories/Maturarbeit/python")
sys.path.append('/Users/nicole/.virtual_python3/lib/python3.6/site-packages/')
from Classes import BServo
from math import degrees

port = "/dev/cu.wchusbserial1d10"
board_id = 2

# DEFINITION SERVOS :
kiefer_servo = BServo(port, board_id, 0)
cube_servo = BServo(port, board_id, 5)


#*****************************************


def my_handler(scene):
    """Handler that get's the Euler X rotation from two cubes and passes this to servos 9 and 10 though the serial port."""

    # Die winkel aus der blender szene holen
    cube_winkel_x = degrees(bpy.data.objects['Cube'].rotation_euler.x)
    cube_winkel_y = degrees(bpy.data.objects['Cube'].rotation_euler.y)


    # Aktionen auf den servos:
    cube_servo.turnAngle(cube_winkel_x)
    kiefer_servo.turnAngle(cube_winkel_y)



# Register the handler to be called once the frame has changed.
bpy.app.handlers.frame_change_post.append(my_handler)

print("fertig")