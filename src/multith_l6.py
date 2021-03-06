import threading

amount = 0


def deposit(dep_amount):
    global amount

    for i in range(dep_amount):
        amount += 1


def two_deposit_threads(dep_amount):
    t1 = threading.Thread(target=deposit,
                          args=(dep_amount,))
    t2 = threading.Thread(target=deposit,
                          args=(dep_amount,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()


two_deposit_threads(10)
print('Balance amount = {0}'.format(amount))
print('Balance amount =', amount)

amount = 0

two_deposit_threads(1000)
print('Balance amount = {0}'.format(amount))

amount = 0

two_deposit_threads(1000000)
print('Balance amount = {0}'.format(amount))

