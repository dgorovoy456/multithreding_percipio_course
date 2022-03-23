import threading
import time


def func():
    time.sleep(2)
    print('\nHello from func! My name is', threading.current_thread().getName())


x = threading.Thread(target=func, name='new_thread')

x.start()
x.join()

print('\nThis is the Main thread. My name is ', threading.current_thread().getName())

print('#####################################')

x = threading.Thread(target=func, name='new_thread')

print(threading.current_thread().getName())

x.start()
x.join()

print('\nThis is the Main thread. My name is ', threading.current_thread().getName())

print('#####################################')


def calc_square(n):
    result = n * n
    print(f'The number {n} squares to {result}')


square_list = []
num_list = [1, 2, 3, 4]

for n in num_list:
    thread = threading.Thread(target=calc_square, args=(n,))
    square_list.append(thread)

    thread.start()
    thread.join()

print('#######################################')


class DerivedThread(threading.Thread):
    def run(self):
        time.sleep(2)
        print('\nHello from func! My name is ', threading.current_thread().getName())


obj = DerivedThread()

obj.start()
obj.join()

print('Control returned to ', threading.current_thread().getName())

print('#########################################')


class RegularClass:
    def print_list(self):
        mixed_list = [7, 6, 11, 'Hello', 5, 2, 'Rose']

        for x in mixed_list:
            print('Printing from child thread: ', x)
            time.sleep(1)


obj = RegularClass()

x = threading.Thread(target=obj.print_list())

x.start()
x.join()

print('Control returned to ', threading.current_thread().getName())
