from datetime import date

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

my_date = date(2024, 9, 24)  # (yyyy, mm, dd)
print(my_date)

d = date(1991, 2, 5)
print(d)
d = d.replace(year=1992, month=1, day=16)
print(d)

d = date(2019, 11, 4)
print(d.weekday())  # 0 is Monday, 6 is Sunday
print(d.isoweekday())  # 1 is Monday, 7 is Sunday

# time(hour, minute, second, microsecond, tzinfo, fold)
from datetime import time

t = time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
