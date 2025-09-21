width = int(input())
height = int(input())

cake_piece = width * height
command = input()

while command != "STOP":
    taken_piece = int(command)
    cake_piece -= taken_piece

    if cake_piece < 0:
        print(f"No more cake left! You need {abs(cake_piece)} pieces more.")
        break

    command = input()

if cake_piece >= 0:
    print(f"{cake_piece} pieces are left.")
