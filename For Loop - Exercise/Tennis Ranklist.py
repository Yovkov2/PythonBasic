import math

numbers = int(input())
points = int(input())

count_win = 0
earned_points = 0

for _ in range(numbers):
    types = input()
    if types == "W":
        earned_points += 2000
        count_win += 1
    elif types == "F":
        earned_points += 1200
    elif types == "SF":
        earned_points += 720

final_points = points + earned_points
average_points = math.floor(earned_points / numbers)
win_percent = count_win / numbers * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")
