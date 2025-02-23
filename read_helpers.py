
import bluetooth
import time
from reader import BLETemperatureCentral


def sleep_ms_flash_led(self, flash_count, delay_ms):
    self._led.off()
    while(delay_ms > 0):
        for i in range(flash_count):
            self._led.on()
            time.sleep_ms(100)
            self._led.off()
            time.sleep_ms(100)
            delay_ms -= 200
        time.sleep_ms(1000)
        delay_ms -= 1000

def print_temp(result, raw):
    print("read temp: %.2f degc" % result)
    print(raw)

def demo(ble, central):
    not_found = False

    def on_scan(addr_type, addr, name):
        if addr_type is not None:
            print("Found sensor: %s" % name)
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

    print("Connected")

    # Explicitly issue reads
    while central.is_connected():
        central.read(callback=print_temp)
        #sleep_ms_flash_led(central, 1, 20)

    print("Disconnected")


def scan_messages(ble, central, callback):
    not_found = False

    def on_scan(addr_type, addr, name):
        if addr_type is not None:
            print("Found sensor: %s" % name)
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

    print("Connected")

    # Explicitly issue reads
    while central.is_connected():
        central.read(callback=print_temp)
        #callback()
        #sleep_ms_flash_led(central, 1, 2000)

    print("Disconnected")

