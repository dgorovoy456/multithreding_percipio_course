import threading

import time


# def greetings_1():
#     for i in range(6):
#         print('Hello')
#         time.sleep(1)
#
#
# def greetings_2():
#     for i in range(6):
#         print('World')
#         time.sleep(1)
#
#
# start_time = time.time()
#
# greetings_1()
# greetings_2()
#
# end_time = time.time()
#
# print('Total time ', end_time - start_time)
#
# print('###############################')


def greetings_3():
    for i in range(6):
        print('Hello')
        time.sleep(1)


def greetings_4():
    for i in range(6):
        print('World')
        time.sleep(1)


start_time = time.time()

t1 = threading.Thread(target=greetings_3)
t2 = threading.Thread(target=greetings_4)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()

print('Total time ', end_time - start_time)
