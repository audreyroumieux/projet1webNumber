import smbus2
import time

bus = smbus2.SMBus(1)

address = 0x04


def write_number(value):
        number = bus.write_byte(address, value)
        time.sleep(1)
        return -1

