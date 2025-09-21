amount = round(float(input()) * 100)

coins = [200, 100, 50, 20, 10, 5, 2, 1]
count = 0

for c in coins:
    if amount == 0:
        break
    count += amount // c
    amount %= c

print(count)