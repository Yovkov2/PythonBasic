import sys

numbers = int(input())
salary = int(input())

for _ in range(1, numbers + 1):
    browse = input()
    if browse == "Facebook":
        salary -= 150
    elif browse == "Instagram":
        salary -= 100
    elif browse == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        sys.exit()

if salary > 0:
    print(salary)