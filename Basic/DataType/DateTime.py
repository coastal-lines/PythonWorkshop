from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

d1 = date(2019, 3, 12)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)

t1 = time(23, 10, 59)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)

dt = datetime(2019, 3, 12, 15, 17)
print(dt)

now = datetime.now()
print(now)

new_dt = now.replace(year=2018)
print(new_dt)

