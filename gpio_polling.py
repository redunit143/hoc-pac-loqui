
import time

from machine import Pin

ACTIVE_VALUE = 1
DEBOUNCE_TIME_MS = 100

"""
p2 = Pin(2, Pin.IN)
p3 = Pin(3, Pin.IN)
p4 = Pin(4, Pin.IN)
p5 = Pin(5, Pin.IN)
p6 = Pin(6, Pin.IN)
p7 = Pin(7, Pin.IN)
p8 = Pin(8, Pin.IN)
p9 = Pin(9, Pin.IN)
p10 = Pin(10, Pin.IN)
p11 = Pin(11, Pin.IN)
p12 = Pin(12, Pin.IN)
p13 = Pin(13, Pin.IN)
p14 = Pin(14, Pin.IN)
p15 = Pin(15, Pin.IN)
p16 = Pin(16, Pin.IN)
p17 = Pin(17, Pin.IN)
p18 = Pin(18, Pin.IN)
p19 = Pin(19, Pin.IN)
p20 = Pin(20, Pin.IN)
p21 = Pin(21, Pin.IN)
p22 = Pin(22, Pin.IN)

pins = { 2: p2 }
"""


def setInputPins(pinNumbers):
    pins = {}
    for i in range(len(pinNumbers)):
        pins.update({pinNumbers[i], Pin(pinNumbers[i], Pin.IN)})
    return pins    


def setOutputPins(pinNumbers):
    pins = {}
    for i in range(len(pinNumbers)):
        pins.update({pinNumbers[i], Pin(pinNumbers[i], Pin.OUT)})
    return pins    


def debounce(thePin):
    for i in range(5):
        while (thePin.value() == ACTIVE_VALUE):
            time.sleep_ms(DEBOUNCE_TIME_MS)


def pollgpio(debug = false):
    for ndx, p in pins.items():
        if (p.value() == ACTIVE_VALUE):
            if debug:
                print(ndx, p, p.value())
            debounce(p)
            return ndx
    return 0;