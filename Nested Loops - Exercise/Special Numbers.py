n = int(input())

for num in range(1111, 10000):
    num_str = str(num)
    is_special = True

    for digit in num_str:
        d = int(digit)
        if d == 0 or n % d != 0:
            is_special = False
            break

    if is_special:
        print(num, end=" ")
