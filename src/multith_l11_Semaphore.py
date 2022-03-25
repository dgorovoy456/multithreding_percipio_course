import threading
import time

semaphore = threading.Semaphore(0)

order_num = 0


def place_order():
    print('Order placed.')
    semaphore.acquire()
    print('Customer order number is: {0}'.format(order_num))


def prepare_order():
    global order_num
    time.sleep(3)
    order_num += 1

    print('Preparing order number {0}'.format(order_num))
    semaphore.release()


for i in range(6):
    t1 = threading.Thread(target=place_order)
    t2 = threading.Thread(target=prepare_order)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

print('#############################################')

semaphore = threading.Semaphore(1)

print(semaphore._value)

semaphore.acquire()

print(semaphore._value)

semaphore.release()

print(semaphore._value)

semaphore.release()

print(semaphore._value)

semaphore.release()

print(semaphore._value)

print('#############################################')

semaphore = threading.BoundedSemaphore(1)

print(semaphore._value)

semaphore.acquire()

print(semaphore._value)

semaphore.release()

print(semaphore._value)

semaphore.release()
