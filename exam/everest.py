current_height = 5364
goal = 8848
days = 1

while True:
    command = input()
    if command == "END":
        break

    meters = int(input())

    if command == "Yes":
        days += 1
        if days > 5:
            break

    current_height += meters

    if current_height >= goal:
        break

if current_height >= goal:
    print(f"Goal reached for {days} days!")
else:
    print(f"Failed!")
    print(f"{current_height}")
