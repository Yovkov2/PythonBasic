hours = int(input())
day = input()

if hours < 10 or hours > 18 or day == "Sunday":
    print("closed")
else:
    print("open")