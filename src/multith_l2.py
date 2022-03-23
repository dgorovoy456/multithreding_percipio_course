import threading
import time


def sleeping_func():
    time.sleep(2)
    print('\nHello from sleeping_func!')


x = threading.Thread(target=sleeping_func, name='brand_new_thread')

x.start()

print(threading.active_count())
print()
print(threading.enumerate())
print()
print(threading.current_thread())

print('\nThis is the Mail thread..')

print('##############################################################\n')

x = threading.Thread(target=sleeping_func, name='brand_new_thread')

x.start()
x.join()

print(threading.active_count())
print()
print(threading.enumerate())
print()
print(threading.current_thread())

print('\nThis is the Mail thread..')

print('##############################################################\n')

x = threading.Thread(target=sleeping_func)
x.start()
x.start()
x.join()

print('Executing by Main thread..')

