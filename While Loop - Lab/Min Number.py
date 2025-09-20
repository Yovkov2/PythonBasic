import sys

command = input()
min_num = sys.maxsize

while command != "Stop":
    new_number = int(command)
    if new_number < min_num:
        min_num = new_number
    command = input()

print(min_num)