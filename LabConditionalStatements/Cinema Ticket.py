day = input()
sum = 0

if day == "Monday" or day == "Tuesday" or day == "Friday":
    sum = 12
elif day == "Wednesday" or day == "Thursday":
    sum = 14
elif day == "Saturday" or day == "Sunday":
    sum = 16

print(sum)