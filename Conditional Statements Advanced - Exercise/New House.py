flower_type = input()
count = int(input())
budjet = int(input())

sum = 0

if flower_type == "Roses":
    sum = count * 5
    if count > 80:
        sum *= 0.90
elif flower_type == "Dahlias":
    sum = count * 3.80
    if count > 90:
        sum *= 0.85
elif flower_type == "Tulips":
    sum = count * 2.80
    if count > 80:
        sum *= 0.85
elif flower_type == "Narcissus":
    sum = count * 3
    if count < 120:
        sum *= 1.15
elif flower_type == "Gladiolus":
    sum = count * 2.50
    if count < 80:
        sum *= 1.20

if budjet >= sum:
    print(f"Hey, you have a great garden with {count} {flower_type} and {budjet-sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {sum-budjet:.2f} leva more.")