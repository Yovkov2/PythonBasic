width = int(input())
height = int(input())
length = int(input())
box = width * height * length
command = input()

while command != "Done":
    lost_box = int(command)
    box -= lost_box
    if box < 0:
        print(f"No more free space! You need {abs(box)} Cubic meters more.")
        break
    command = input()

if box >= 0:
    print(f"{box} Cubic meters left.")