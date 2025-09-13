house = int(input())
minutes = int(input()) + 15

if minutes > 59:
    house+=1
    minutes -= 60
if house > 23:
    house = 0

if minutes < 10:
    print(f"{house}:0{minutes}")
else:
    print(f"{house}:{minutes}")