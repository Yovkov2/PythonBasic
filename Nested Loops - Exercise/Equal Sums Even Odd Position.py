start = int(input())
end = int(input())

for number in range(start, end + 1):
    num_str = str(number)
    even_sum = 0
    odd_sum = 0
    for i in range(6):
        digit = int(num_str[i])
        if (i + 1) % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(number, end=" ")
    