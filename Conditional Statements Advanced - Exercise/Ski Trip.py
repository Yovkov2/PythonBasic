day_count = int(input()) - 1
type_room = input()
grade = input()

total = 0

if type_room == "room for one person":
    total = day_count * 18
elif type_room == "apartment":
    total = day_count * 25
    if day_count < 10:
        total *= 0.70
    elif 10 <= day_count <= 15:
        total *= 0.65
    else:
        total *= 0.50
elif type_room == "president apartment":
    total = day_count * 35
    if day_count < 10:
        total *= 0.90
    elif 10 <= day_count <= 15:
        total *= 0.85
    else:
        total *= 0.80

if grade == "positive":
    total *= 1.25
else:
    total *= 0.90

print(f"{total:.2f}")
