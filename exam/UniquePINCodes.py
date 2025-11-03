first_limit = int(input())
second_limit = int(input())
third_limit = int(input())
for first in range(1, first_limit + 1):
    for second in range(1, second_limit + 1):
        for third in range(1, third_limit + 1):
            if first % 2 == 0 and third % 2 == 0 and second in (2,3,5,7):
                print(f"{first} {second} {third}")