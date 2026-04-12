import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(1, my_time)):
    print(x)
    time.sleep(1)

print("Time is up!")

for y in range(my_time, 0, -1):
    print(y)
    time.sleep(1)
print("Done!")

for z in range(my_time, 0, -1):
    seconds = z % 60
    minutes = (z // 60) % 60
    hours = (z // 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("200")