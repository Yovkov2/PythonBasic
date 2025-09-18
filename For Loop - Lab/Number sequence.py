numbers = int(input())

num = int(input())
min_num = num
max_num = num

for _ in range(numbers-1):
    num = int(input())
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")