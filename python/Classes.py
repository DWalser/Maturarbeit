import serial
import time


class BServo(object):

    write_time_out = 0.05
    angle_tolerance = 1.0

    def __init__(self, port, board_id, servo_nr, lowvalue=45, highvalue=135, range=90):
        if board_id < 0 or board_id > 15:
            raise ValueError("wrong board id")
        if servo_nr < 0 or servo_nr > 15:
            raise ValueError("wrong servo number")

        self.board_id   = board_id  # id of the servo board
        self.servo_nr   = servo_nr  # servo channel on board
        self.lowvalue   = lowvalue  # low value of movement
        self.highvalue  = highvalue # high value of movement
        self.range      = range     # degree range of movement
        #self.inverted   = inverted  # if true, movenent is inverted

        self.servo_id = self.board_id << 4 | self.servo_nr

        self.serial = serial.Serial(port)

        self._time_last_write = 0
        self._last_transmitted_angle = 0

    def __del__(self):
        self.serial.close()

    def angle(self, value):
        """
        calculates the servo angle according to the blender scene value.
        :param value:
        :return:
        """
        valuerange = self.highvalue - self.lowvalue
        lowangle = 90 - 1. * self.range/2.
        highangle = 90 + 1. * self.range/2.
        m = 1.*(highangle-lowangle)/valuerange
        q = highangle - m*self.highvalue
        return m * value + q

    def turnValue(self, value):
        self.turnAngle(self.angle(value=value))

    def turnAngle(self, angle):
        if self.out_of_dead_time() and self.is_new_angle(angle):
            angle = self.int_angle_in_range(angle)
            self.serial.write(('S' + chr(self.servo_id) + chr(angle)).encode('latin_1'))

            self._last_transmitted_angle = angle
            self._time_last_write = time.time()

            #while not self.serial.in_waiting:
            #    time.sleep(0.1)
            #print(self.serial.read_all())

    def int_angle_in_range(self, angle):
        min_angle = 90. - 1. * self.range / 2.
        max_angle = 90. + 1. * self.range / 2.
        if angle < min_angle:
            new_angle = min_angle
        elif angle > max_angle:
            new_angle = max_angle
        else:
            new_angle = angle
        return int(new_angle)

    def out_of_dead_time(self):
        return time.time() > self._time_last_write + BServo.write_time_out

    def is_new_angle(self, angle):
        int_angle = self.int_angle_in_range(angle)
        return not (self._last_transmitted_angle - self.angle_tolerance < int_angle < self._last_transmitted_angle + self.angle_tolerance)

    def toDefaultPosition(self):
        self.turnAngle(90)
