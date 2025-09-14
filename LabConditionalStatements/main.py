import sys

day = int(input())
day_ofWeek = ""

if day == 1:
    day_ofWeek = "Monday"
elif day == 2:
    day_ofWeek = "Tuesday"
elif day == 3:
    day_ofWeek = "Wednesday"
elif day == 4:
    day_ofWeek = "Thursday"
elif day == 5:
    day_ofWeek = "Friday"
elif day == 6:
    day_ofWeek = "Saturday"
elif day == 7:
    day_ofWeek = "Sunday"
elif day < 1 or day > 7:
    day_ofWeek = "Error"


print(day_ofWeek)