
import bluetooth
import time
from reader import BLETemperatureCentral

from machine import Pin

ACTIVE_VALUE = 1
DEBOUNCE_TIME_MS = 100

#pins = (0,1,2,3,4,5,6,7,8)
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

#pins = { 2: p2, 3:p3, 4:p4, 5:p4, 6:p6, 7:p7, 8:p8, 9:p9, 10:p10, 11:p11, 12:p12, 13:p13, 14:p14, 15:p15, 16:p16, 17:p17, 18:p18, 19:p19, 20:p20, 21:p21, 22:p22 }
pins = { 2: p2 }
def debounce(p):
    for i in range(5):
        while (p.value() == ACTIVE_VALUE):
            time.sleep_ms(DEBOUNCE_TIME_MS)
            print(i, p.value(), p)
        
    
    
def pollgpio():
    for ndx, p in pins.items():
        if (p.value() == ACTIVE_VALUE):
            print(ndx, p, p.value())
            debounce(p)
            return ndx
        #print(ndx, p)
    return 0;