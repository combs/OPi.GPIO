from __future__ import print_function

import pyA20
from pyA20.gpio import gpio
from pyA20.gpio import port


class GPIO(object):

    OUT = gpio.OUTPUT
    IN = gpio.INPUT
    HIGH = 1
    LOW = 0

    def __init__(self):
        gpio.init()
        print("hi")

    def setup(self,port,mode):
        gpio.setcfg(port,mode)

    def output(self,port,value): 
        gpio.output(port,value)

    def input(self,port,value):
        return gpio.input(port,value)
