import time
from datetime import date

timestamp = time.time()
print("Timestamp:", timestamp)
d = date.fromtimestamp(timestamp)
print("Date:", d)

timestamp = 1572879180
print(time.ctime(timestamp))
print(time.ctime())


class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")


student = Student()
student.take_nap(5)
