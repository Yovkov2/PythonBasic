price = float(input())
puzzles = float(input())
kukla = float(input())
bear = float(input())
minions = float(input())
tir = float(input())

puzzles_sum = puzzles * 2.60
kukla_sum = kukla * 3
bear_sum = bear * 4.10
minions_sum = minions * 8.20
tir_sum = tir * 2

total_sum = puzzles_sum + kukla_sum + bear_sum + minions_sum + tir_sum

if puzzles + kukla + bear + minions + tir >= 50:
    total_sum *= 0.75

total_sum *= 0.90

if total_sum >= price:
    print(f"Yes! {total_sum-price:.2f} lv left.")
else:
    print(f"Not enough money! {price-total_sum:.2f} lv needed.")