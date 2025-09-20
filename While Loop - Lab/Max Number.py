import sys

command = input()
max_num = -sys.maxsize

while command != "Stop":
    new_number = int(command)
    if new_number > max_num:
        max_num = new_number
    command = input()

print(max_num)