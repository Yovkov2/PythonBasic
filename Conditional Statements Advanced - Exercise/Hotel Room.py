month = input()
count_nights = int(input())

studio_sum = 0
apartament_sum = 0

if month == "May" or month == "October":
    studio_sum = count_nights * 50
    apartament_sum = count_nights * 65
    if count_nights > 14:
        studio_sum *= 0.70
    elif count_nights > 7:
        studio_sum *= 0.95

elif month == "June" or month == "September":
    studio_sum = count_nights * 75.20
    apartament_sum = count_nights * 68.70
    if count_nights > 14:
        studio_sum *= 0.80

elif month == "July" or month == "August":
    studio_sum = count_nights * 76
    apartament_sum = count_nights * 77

if count_nights > 14:
    apartament_sum *= 0.90

print(f"Apartment: {apartament_sum:.2f} lv.")
print(f"Studio: {studio_sum:.2f} lv.")
