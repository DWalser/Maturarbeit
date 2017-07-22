import sys
sys.path.append("/Users/nicole/Repositories/Maturarbeit/python")
sys.path.append('/Users/nicole/.virtual_python3/lib/python3.6/site-packages/')
from Classes import BServo

port = "/dev/cu.wchusbserial1d10"
board_id = 2

kiefer = BServo(port, board_id, 0)
auge_rechts = BServo(port, board_id, 1)


