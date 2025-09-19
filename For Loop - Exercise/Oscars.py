import sys

actor_name = input()
points_academy = float(input())
numbers = int(input())

for _ in range(1, numbers + 1):
    name = input()
    points = float(input())

    points_academy += (len(name) * points) / 2
    if points_academy >=1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points_academy:.1f}!")
        sys.exit()


if points_academy < 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - points_academy:.1f} more!")