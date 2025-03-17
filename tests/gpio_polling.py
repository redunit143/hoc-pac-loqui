
from machine import Pin


def test(x):
    p = x((2,4))
    if p.get(2) == Pin(2, Pin.IN) and p.get(4) == Pin(4, Pin.IN):
        print(".")
    else:
        print("FAILED")



def test(x):
    p = x((2,4))
    if p.get(2) == Pin(2, Pin.OUT) and p.get(4) == Pin(4, Pin.OUT):
        print(".")
    else:
        print("FAILED")
