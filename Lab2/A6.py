sec = int(input())
min = 0
hour = 0
while sec >= 60:
    sec -= 60
    min += 1
while min >= 60:
    min -= 60
    hour += 1
while hour >= 24:
    hour = 0
print('{}:{:02}:{:02}'.format (hour,min,sec))