import sys
import bpy
sys.path.append("/Users/nicole/Repositories/Maturarbeit/python")
sys.path.append('/Users/nicole/.virtual_python3/lib/python3.6/site-packages/')
from Classes import BServo
from math import degrees

port = "/dev/cu.wchusbserial1d10"
board_id = 2

quader= BServo(port, board_id, 2)

def my_handler(scene):

    quader_winkel_y = degrees(bpy.data.objects['quader'].rotation_euler.y)
    quader.turnAngle(quader_winkel_y)

bpy.app.handlers.frame_change_post.append(my_handler)

print("fertig")