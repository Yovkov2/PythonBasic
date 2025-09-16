budjet = int(input())
season = input()
count_fisherman = int(input())
sum = 0

if season == "Spring":
    sum = 3000
elif season == "Summer" or season == "Autumn":
    sum = 4200
elif season == "Winter":
    sum = 2600

if count_fisherman <= 6:
    sum *= 0.90
elif count_fisherman > 7 and count_fisherman <= 11:
    sum *= 0.85
elif count_fisherman > 11:
    sum *= 0.75

if (count_fisherman % 2 == 0) and not season == "Autumn":
    sum *= 0.95

if budjet >= sum:
    print(f"Yes! You have {budjet-sum:.2f} leva left.")
else:
    print(f"Not enough money! You need {sum-budjet:.2f} leva.")