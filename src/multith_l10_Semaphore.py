import time
import threading

semaphore = threading.Semaphore()


def my_func():
    semaphore.acquire()
    time.sleep(0.1)
    print(threading.current_thread().name, ' acquired the semaphores')
    print('Semaphore value after acquire: ', semaphore._value)

    time.sleep(5)

    semaphore.release()

    print('Semaphore value after release: ', semaphore._value)


# t1 = threading.Thread(target=my_func)
# t2 = threading.Thread(target=my_func)
#
# print('Initial semaphore value : ', semaphore._value)

# start_time = time.time()
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# end_time = time.time()
#
# print('Total time: ', end_time - start_time)

semaphore = threading.Semaphore(value=3)

t1 = threading.Thread(target=my_func)
t2 = threading.Thread(target=my_func)
t3 = threading.Thread(target=my_func)
t4 = threading.Thread(target=my_func)
t5 = threading.Thread(target=my_func)
t6 = threading.Thread(target=my_func)
t7 = threading.Thread(target=my_func)
t8 = threading.Thread(target=my_func)

start_time = time.time()

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

end_time = time.time()

print('Total time: ', end_time - start_time)
