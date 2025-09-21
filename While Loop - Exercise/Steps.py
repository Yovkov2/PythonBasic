command = input()
sum_step = 0
while command != "Going home":
    steps = int(command)
    sum_step += steps
    if sum_step >= 10000:
        print(f"Goal reached! Good job!")
        print(f"{sum_step - 10000} steps over the goal!")
        break
    command = input()

if command == "Going home":
    more_step = int(input())
    sum_step += more_step
    if sum_step >= 10000:
        print("Goal reached! Good job!")
        print(f"{sum_step - 10000} steps over the goal!")
    else:
        print(f"{10000 - sum_step} more steps to reach goal.")