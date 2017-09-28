import sys
import bpy
sys.path.append("/Users/nicole/Repositories/Maturarbeit/python")
sys.path.append('/Users/nicole/.virtual_python3/lib/python3.6/site-packages/')
from Classes import BServo
from math import degrees

port = "/dev/cu.wchusbserialfd120"
board_id = 2

# DEFINITION SERVOS :
A_servo = BServo(port, board_id, 0)
B_servo = BServo(port, board_id, 1)
C_servo = BServo(port, board_id, 2)
D_servo = BServo(port, board_id, 3)

def my_handler(scene):

    cube_winkel_a = degrees(bpy.data.objects['Cube'].rotation_euler.x)
    cube_winkel_b = degrees(bpy.data.objects['Cube.001'].rotation_euler.x)
    cube_winkel_c = degrees(bpy.data.objects['Cube.002'].rotation_euler.x)
    cube_winkel_d = degrees(bpy.data.objects['Cube.003'].rotation_euler.x)
    A_servo.turnAngle(cube_winkel_a)
    B_servo.turnAngle(cube_winkel_b)
    C_servo.turnAngle(cube_winkel_c)
    D_servo.turnAngle(cube_winkel_d)

bpy.app.handlers.frame_change_post.append(my_handler)

print("fertig")