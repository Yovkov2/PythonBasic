number = int(input())

current = 1
row = 1
while current <= number:
    for i in range(row):
        if current > number:
            break
        print(current, end=" ")
        current += 1
    print()
    row += 1