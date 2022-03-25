import threading
import time
from pprint import pprint

event = threading.Event()

pprint(dir(event))

event.set()

print(event.is_set())
print(event.isSet())

event.wait()

print(event.is_set())

event.clear()

print(event.is_set())

# print('##############################')
#
# event.set()
# print(event.is_set())
# event.clear()
# print(event.is_set())
# event.wait()
# print(event.is_set())

print('#####################################')

meeting = threading.Event()


def hold_meeting():
    meeting.set()
    print('Event is set. The meeting has begun')

    time.sleep(6)

    print('The meeting is compleate. Clearing the event...')
    meeting.clear()


def enter_conference_room():
    time.sleep(1)
    meeting.wait()

    while meeting.is_set():
        print('Waiting for meeting to end')
        time.sleep(0.5)

    print('The meeting is done. Entering the conference room')


t1 = threading.Thread(target=hold_meeting)
t2 = threading.Thread(target=enter_conference_room)

t1.start()
t2.start()

t1.join()
t2.join()
