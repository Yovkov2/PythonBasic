import sys

numbers = int(input())
max_num = -sys.maxsize
sum = 0

for num in range(1, numbers + 1):
    new_num = int(input())
    if new_num > max_num:
        max_num = new_num
    sum += new_num

if max_num == sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - (sum - max_num))
    print("No")
    print(f"Diff = {diff}")