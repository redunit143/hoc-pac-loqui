
import bluetooth
import time
from reader import BLETemperatureCentral, scan_messages, processData
from writer import BLETemperature
from read_helpers import demo
from gio_buttons import pollgpio
from messages import message, send_message, msgcat

from machine import Pin

    
def scan_messagesx(ble, central, scanCallback):
    not_found = False

    def on_scan(addr_type, addr, name):
        if addr_type is not None:
            print("Found sensor for scanning: %s" % name)
            central.connect()
        else:
            nonlocal not_found
            not_found = True
            print("No sensor found.")

    central.scan(callback=on_scan)

    # Wait for connection...
    while not central.is_connected():
        time.sleep_ms(100)
        if not_found:
            return

    print("Connected for scan")

    # Explicitly issue reads
    while central.is_connected():
        central.read(callback=scanCallback)
        #callback()
        time.sleep_ms(200)

    print("Disconnected")


if __name__ == "__main__":
    msg_counter = 0;
    category = msgcat.DEFAULT
    def abc(a,b):
        #p2 = Pin(2, Pin.IN)
        #print(p2.value())
        print(a,b)
        time.sleep_ms(500)
 
    led = Pin('LED', Pin.OUT)
    led.toggle()
    ble = 0;
    central = 0
    loop_count = 0;
    
    if False: # send on gpio        
        ble = bluetooth.BLE()
        temp = BLETemperature(ble)
        while(True):
            loop_count += 1
            if (loop_count % 20 == 0):
                led.toggle()
                loop_count = 0

            ndx = pollgpio()
            if ndx != 0:
                msg_counter += 1
                send_message(ble, temp, msg_counter, category, ndx)
                print(message(ndx), ndx, msg_counter)
    else: # read bluetooth comms
        ble = bluetooth.BLE()
        central = BLETemperatureCentral(ble)
        while(True):
            scan_messages(ble, central, processData)
            #demo(ble, central)
            sleep_ms(1000)
            print("--------------------")
        

