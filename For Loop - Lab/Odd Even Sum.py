n = int(input())

odd_sum = 0
even_sum = 0

for i in range(n):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    diff = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {diff}")