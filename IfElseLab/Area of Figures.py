import  math

figure = input()
first_number = float(input())

if figure == "square":
    print(f"{first_number * first_number:.3f}")
elif figure == "circle":
    print(f"{math.pi * (first_number ** 2):.3f}")
elif figure == "rectangle":
    second_number = float(input())
    print(f"{first_number * second_number:.3f}")
else:
    second_number = float(input())
    print(f"{(first_number * second_number)/2:.3f}")