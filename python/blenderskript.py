import sys
import bpy
sys.path.append("/Users/nicole/Repositories/Maturarbeit/python")
sys.path.append('/Users/nicole/.virtual_python3/lib/python3.6/site-packages/')
from Classes import BServo
from math import degrees

port = "/dev/cu.wchusbserialfd120"
board_id = 2

# DEFINITION SERVOS :
kiefer_servo = BServo(port, board_id, 0)
cube_servo = BServo(port, board_id, 1)

def my_handler(scene):

    cube_winkel_x = degrees(bpy.data.objects['Cube'].rotation_euler.x)
    cube_winkel_y = degrees(bpy.data.objects['Cube'].rotation_euler.y)
    cube_servo.turnAngle(cube_winkel_x)
    kiefer_servo.turnAngle(cube_winkel_y)

bpy.app.handlers.frame_change_post.append(my_handler)

print("fertig")