budjet = float(input())
statists = int(input())
price_statists = float(input())

dekor = budjet * 0.10
sum = statists * price_statists
if statists > 150 :
    sum *= 0.90

total = sum + dekor
if budjet >= total:
    print("Action!")
    print(f"Wingard starts filming with {budjet-total:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total-budjet:.2f} leva more.")