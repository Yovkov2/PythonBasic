budjet = float(input())
city = input()
season = input()
days = int(input())
sum = 0

if city == "Dubai":
    if season == "Winter":
        sum = days * 45000
    elif season == "Summer":
        sum = days * 40000
elif city == "Sofia":
    if season == "Winter":
        sum = days * 17000
    elif season == "Summer":
        sum = days * 12500
elif city == "London":
    if season == "Winter":
        sum = days * 24000
    elif season == "Summer":
        sum = days * 20250

if city == "Dubai":
    sum *= 0.70
elif city == "Sofia":
    sum *= 1.25

if budjet >= sum:
    print(f"The budget for the movie is enough! We have {budjet-sum:.2f} leva left!")
else:
    print(f"The director needs {sum - budjet:.2f} leva more!")