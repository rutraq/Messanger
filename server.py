from threading import Thread
from time import sleep
import client


def threaded_function():
    client.get_message()
    

def thread_func(arg2):
    for i in range(arg2):
        print("sos")
        sleep(3)


if __name__ == "__main__":
    thread = Thread(target=threaded_function)
    thread2 = Thread(target=thread_func, args=(30, ))
    thread.start()
    print("thread finished...exiting")
    while True:
        print("sos")
        sleep(3)
