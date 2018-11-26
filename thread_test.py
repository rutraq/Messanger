import time
import easygui
from multiprocessing import Process
import client


def login_with_sql():
    client.get_message()


def send():
    while True:
        print("sos")
        time.sleep(2)


if __name__ == '__main__':
    proc = Process(target=login_with_sql)
    proc.start()
    proc2 = Process(target=send)
    proc2.start()
