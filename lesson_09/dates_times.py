import datetime

date = datetime.date(2026, 4, 21)
print(date)

today = datetime.date.today()
print(today)

time = datetime.time(17, 5, 26)
print(time)

now = datetime.datetime.now()
print(now)

now = now.strftime("%H:%M:%S %d.%m.%Y")
print(now)

target_datetime = datetime.datetime(2030, 1, 4, 9, 0, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")