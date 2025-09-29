import math
tenis_raketa = float(input())
count_raketa = int(input())
count_shoes = int(input())

sum_raketi = tenis_raketa * count_raketa
sum_shoes = count_shoes * (tenis_raketa / 6)
sum_total = sum_raketi + sum_shoes
sum_total += sum_total * 0.2
djokovic = math.floor(sum_total / 8)
sponsors = math.ceil(sum_total * 7 / 8)

print(f"Price to be paid by Djokovic {djokovic}")
print(f"Price to be paid by sponsors {sponsors}")