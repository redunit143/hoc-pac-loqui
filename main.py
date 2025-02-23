
import bluetooth
import time
from reader import BLETemperatureCentral
from writer import BLETemperature
from read_helpers import demo, scan_messages
from gio_buttons import pollgpio
from messages import message, send_message, msgcat

from machine import Pin



if __name__ == "__main__":
    msg_counter = 0;
    category = msgcat.DEFAULT
    def abc():
        #p2 = Pin(2, Pin.IN)
        #print(p2.value())
        time.sleep_ms(500)
 
    ble = bluetooth.BLE()
    temp = BLETemperature(ble)

    #ble = bluetooth.BLE()
    #central = BLETemperatureCentral(ble)
        
    ble = 0;
    central = 0
    while(True):
        #demo(ble, central)
        #scan_messages(ble, central, abc)
       ndx = pollgpio()
       if ndx != 0:
           msg_counter += 1
           send_message(ble, temp, msg_counter, category, ndx)
           print(message(ndx), ndx, msg_counter)
