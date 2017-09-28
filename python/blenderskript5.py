import sys
import bpy
sys.path.append("/Users/nicole/Repositories/Maturarbeit/python")
sys.path.append('/Users/nicole/.virtual_python3/lib/python3.6/site-packages/')
from Classes import BServo
from math import degrees

port = "/dev/cu.wchusbserial1d10"
board_id = 2

# DEFINITION SERVOS :
eins= BServo(port, board_id, 0)
zwei= BServo(port, board_id, 1)
drei= BServo(port, board_id, 3)

def my_handler(scene):

    eins_winkel_x = degrees(bpy.data.objects['eins'].rotation_euler.x)
    zwei_winkel_x = degrees(bpy.data.objects['zwei'].rotation_euler.x)
    drei_winkel_x = degrees(bpy.data.objects['drei'].rotation_euler.x)
    eins.turnAngle(eins_winkel_x)
    zwei.turnAngle(zwei_winkel_x)
    drei.turnAngle(drei_winkel_x)

bpy.app.handlers.frame_change_post.append(my_handler)

print("fertig")