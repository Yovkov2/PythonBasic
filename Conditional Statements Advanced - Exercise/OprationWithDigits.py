import sys

first_number = int(input())
second_number = int(input())
opperator = input()
sum = 0

if opperator == '+':
    sum = first_number + second_number
    if sum % 2 == 0:
        print(f"{first_number} + {second_number} = {sum} - even")
    else:
        print(f"{first_number} + {second_number} = {sum} - odd")
elif opperator == '-':
    sum = first_number - second_number
    if sum % 2 == 0:
        print(f"{first_number} - {second_number} = {sum} - even")
    else:
        print(f"{first_number} - {second_number} = {sum} - odd")
elif opperator == '*':
    sum = first_number * second_number
    if sum % 2 == 0:
        print(f"{first_number} * {second_number} = {sum} - even")
    else:
        print(f"{first_number} * {second_number} = {sum} - odd")
elif opperator == '/':
    if first_number == 0:
        print(f"Cannot divide {second_number} by zero")
        sys.exit()
    elif second_number == 0:
        print(f"Cannot divide {first_number} by zero")
        sys.exit()
    else:
        print(f"{first_number} / {second_number} = {first_number/second_number:.2f}")
elif opperator == '%':
    if first_number == 0:
        print(f"Cannot divide {second_number} by zero")
        sys.exit()
    elif second_number == 0:
        print(f"Cannot divide {first_number} by zero")
        sys.exit()
    else:
        print(f"{first_number} % {second_number} = {first_number%second_number}")
