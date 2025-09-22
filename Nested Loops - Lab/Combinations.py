n = int(input())

count = 0

for x1 in range(n + 1):
    for x2 in range(n + 1):
        x3 = n - (x1 + x2)
        if x3 >= 0:
            count += 1

print(count)
