import threading
import time

data_one = 3
data_two = 5


# def my_process_with_dead_lock(lock_one, lock_two):
#     global data_one
#     global data_two
#
#     lock_one.acquire()
#     print(threading.current_thread().name, ' incrementing data_one')
#     data_one += 1
#     time.sleep(1)
#
#     lock_two.acquire()
#     print(threading.current_thread().name, ' incrementing data_two')
#     data_two += 1
#     time.sleep(1)
#
#     lock_one.release()
#     lock_two.release()
#
#
# lock_one = threading.Lock()
# lock_two = threading.Lock()
#
# t1 = threading.Thread(target=my_process_with_dead_lock, args=(lock_one, lock_two))
#
# t2 = threading.Thread(target=my_process_with_dead_lock, args=(lock_two, lock_one))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

# print('########################################')

# def my_process_without_dead_lock(lock_one, lock_two):
#     global data_one
#     global data_two
#
#     lock_one.acquire()
#     print(threading.current_thread().name, ' incrementing data_one')
#     data_one += 1
#     time.sleep(1)
#
#     lock_two.acquire()
#     print(threading.current_thread().name, ' incrementing data_two')
#     data_two += 1
#     time.sleep(1)
#
#     lock_one.release()
#     lock_two.release()
#
#
# lock_one = threading.Lock()
# lock_two = threading.Lock()
#
# t1 = threading.Thread(target=my_process_without_dead_lock, args=(lock_one, lock_two))
#
# t2 = threading.Thread(target=my_process_without_dead_lock, args=(lock_one, lock_two))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print('data_one: {0}'.format(data_one))
# print('data_two: {0}'.format(data_two))

# print('########################################')

def my_process_with_avoiding_dead_lock(lock_one, lock_two):
    global data_one
    global data_two

    lock_one.acquire()
    print(threading.current_thread().name, ' incrementing data_one')
    data_one += 1
    time.sleep(1)

    lock_one.release()

    lock_two.acquire()
    print(threading.current_thread().name, ' incrementing data_two')
    data_two += 1
    time.sleep(1)

    lock_two.release()


lock_one = threading.Lock()
lock_two = threading.Lock()

t1 = threading.Thread(target=my_process_with_avoiding_dead_lock, args=(lock_one, lock_two))

t2 = threading.Thread(target=my_process_with_avoiding_dead_lock, args=(lock_two, lock_one))

t1.start()
t2.start()

t1.join()
t2.join()

print('data_one: {0}'.format(data_one))
print('data_two: {0}'.format(data_two))
