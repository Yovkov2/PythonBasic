people = int(input())
season = input()
total_sum = 0

if season == "spring":
    if people <= 5:
        total_sum = people * 50
    elif people > 5:
        total_sum = people * 48
elif season == "autumn":
    if people <= 5:
        total_sum = people * 60
    elif people > 5:
        total_sum = people * 49.50
elif season == "summer":
    if people <= 5:
        total_sum = people * 48.50
    elif people > 5:
        total_sum = people * 45
    total_sum *= 0.85
elif season == "winter":
    if people <= 5:
        total_sum = people * 86
    elif people > 5:
        total_sum = people * 85
    total_sum *= 1.08

print(f"{total_sum:.2f} leva.")

