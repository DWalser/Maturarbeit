import sys
import bpy
sys.path.append("/Users/nicole/Repositories/Maturarbeit/python")
sys.path.append('/Users/nicole/.virtual_python3/lib/python3.6/site-packages/')
from Classes import BServo
from math import degrees

port = "/dev/cu.wchusbserial1d10"
board_id = 2

# DEFINITION SERVOS :
A_servo = BServo(port, board_id, 0)
B_servo = BServo(port, board_id, 5)
C_servo = BServo(port, board_id, 6)
D_servo = BServo(port, board_id, 7)

def my_handler(scene):

    cube_winkel_x = degrees(bpy.data.objects['Cube01'].rotation_euler.x)
    cube_winkel_y = degrees(bpy.data.objects['Cube02'].rotation_euler.y)
    cube_winkel_z = degrees(bpy.data.objects['Cube03'].rotation_euler.z)
    cube_winkel_x = degrees(bpy.data.objects['Cube04'].rotation_euler.x)
    A_servo.turnAngle(cube_winkel_x)
    B_servo.turnAngle(cube_winkel_y)
    C_servo.turnAngle(cube_winkel_z)
    D_servo.turnAngle(cube_winkel_x)

bpy.app.handlers.frame_change_post.append(my_handler)

print("fertig")