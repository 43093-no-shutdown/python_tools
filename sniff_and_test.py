#if you need sniff packets and do test by python, you can try it.
#if you need any help, please tell me. thank you.

import pyshark
from time import sleep
import threading


def sniff_packets():
    cap = pyshark.LiveCapture(interface = 'wlp3s0')
    for i in cap.sniff_continuously():
        print('verify packet: highest_layer',i.highest_layer)

def test():
    for i in range(5):
        sleep(1)
        print("do your test ",i)


if __name__ == '__main__':
    t1 = threading.Thread(target=sniff_packets,args=())
    t1.setDaemon(True)
    t1.start()
    test()
