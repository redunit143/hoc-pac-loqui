
import time

from machine import Pin
"""
gpio pins 2 to 22 in pico
"""
ACTIVE_VALUE = 1
DEBOUNCE_TIME_MS = 100


def setInputPins(pinNumbers):
    pins = {}
    for i in range(len(pinNumbers)):
        pNo = pinNumbers[i]
        pins.update({pNo: Pin(pNo, Pin.IN)})
    return pins    


def setOutputPins(pinNumbers):
    pins = {}
    for i in range(len(pinNumbers)):
        pNo = pinNumbers[i]
        pins.update({pNo: Pin(pNo, Pin.OUT)})
    return pins    


def debounce(thePin):
    for i in range(5):
        while (thePin.value() == ACTIVE_VALUE):
            time.sleep_ms(DEBOUNCE_TIME_MS)


def pollgpio(debug = False):
    for ndx, p in pins.items():
        if (p.value() == ACTIVE_VALUE):
            if debug:
                print(ndx, p, p.value())
            debounce(p)
            return ndx
    return 0;