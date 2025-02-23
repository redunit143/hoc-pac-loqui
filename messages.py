messages = [
    "0", #0
    "-", #1
    "pin 2", #2
    "pin 3", #3
    "pin 4", #4
    "pin 5", #5
    "pin 6", #6
    "pin 7", #7
    "pin 8", #8
    "pin 9", #9
    "pin 10", #10
    "pin 11", #11
    "pin 12", #12
    "pin 13", #13
    "pin 14", #14
    "pin 15", #15
    "pin 16", #16
    "pin 17", #17
    "pin 18", #18
    "pin 19", #19
    "pin 20", #20
    "pin 21", #21
    "pin 22", #22
    "n/a (23) ", #
    "n/a (24) ", #
    "n/a (25) ", #
    "pin 26", #26
    "pin 27", #27
    "pin 28", #28
    
    ];

class msgcat:
    DEFAULT = 0

def message(ndx):
    if  not ndx:
        return None
    return messages[ndx]
#    return "test"


def send_message(ble, temp, msg_counter, category, ndx):
    data = category + (ndx * 10) + ((msg_counter % 100) * 100)
    print('Sending: ', data)
    temp.send(data, notify=True, indicate=False)
    return 1;