budjet = float(input())
nights = int(input())
night_price = float(input())
add_razhod = int(input())

if nights > 7:
    night_price *= 0.95
total_nights = nights * night_price
extra = budjet * add_razhod / 100

sum = total_nights + extra

if budjet >= sum:
    print(f"Ivanovi will be left with {budjet - sum:.2f} leva after vacation.")
else:
    print(f"{sum - budjet:.2f} leva needed.")