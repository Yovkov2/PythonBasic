budget = float(input())
count = int(input())
price = float(input())

decor_sum = budget * 0.1
clothes_sum = count * price

if count > 150:
    clothes_sum *= 0.90   # отстъпка 10%

total_sum = decor_sum + clothes_sum

if budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_sum:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_sum - budget:.2f} leva more.")
