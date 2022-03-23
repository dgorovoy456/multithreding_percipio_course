import threading

# amount = 0


# def deposit(dep_amount, dep_lock):
#     global amount
#
#     for i in range(dep_amount):
#         dep_lock.acquire(timeout=3)
#         amount += 1
#         dep_lock.release()
#
#
# def two_deposit_threads(dep_amount):
#
#     lock = threading.Lock()
#
#     t1 = threading.Thread(target=deposit,
#                           args=(dep_amount, lock))
#     t2 = threading.Thread(target=deposit,
#                           args=(dep_amount, lock))
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#
# two_deposit_threads(1000000)
# print('Balance amount = {0}'.format(amount))

print('###############################')

# lock = threading.Lock()
#
# print('First try: ', lock.acquire())
# print('Second try: ', lock.acquire())

print('###############################')

lock = threading.Lock()

print('First try: ', lock.acquire())
print('Second try: ', lock.acquire(timeout=3))

print('###############################')

lock = threading.RLock()

print('First try: ', lock.acquire())
print('Second try: ', lock.acquire())




