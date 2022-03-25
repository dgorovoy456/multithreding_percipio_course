import random
import threading
import time

condition = threading.Condition()

container = []

counter = 1

more_to_come = True


def produce():
    global container
    global counter
    global more_to_come

    for i in range(5):
        time.sleep(random.randrange(2, 5))
        condition.acquire()

        item = 'News item #' + str(counter)

        container.append(item)
        counter += 1

        print('\nProduced', item)
        condition.notify_all()

        condition.release()

    more_to_come = False


def consume():
    global more_to_come

    while (more_to_come):
        condition.acquire()
        condition.wait()

        time.sleep(random.random())
        print(threading.current_thread().getName(), ' acquired:', container[-1])

        condition.release()


producer_thread = threading.Thread(target=produce)

consumer_one_thread = threading.Thread(target=consume, name='News Site One')
consumer_two_thread = threading.Thread(target=consume, name='News Site two')
consumer_three_thread = threading.Thread(target=consume, name='News Site Three')

threads = [producer_thread,
           consumer_one_thread,
           consumer_two_thread,
           consumer_three_thread,
           ]

for t in threads:
    t.start()

for t in threads:
    t.join()

time.sleep(1)
print('\nAll done')
