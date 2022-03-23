import threading
from pprint import pprint


def new_func():
    pprint(threading.active_count())
    print()
    pprint(threading.enumerate())
    print()
    pprint(threading.current_thread())


new_func()


def func():
    print('Hello from func: \n')


x = threading.Thread()
x.start()

x = threading.Thread(target=func)
x.start()
