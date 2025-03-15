"""
from ... gpio_polling import *

pins = setInputPins((2))
"""

from machine import Pin


def test(x):
    p = x((2,4))
    if p.get(2) == Pin(2, Pin.IN) and p.get(4) == Pin(3, Pin.IN):
        print(".")
    else:
        print("FAILED")
