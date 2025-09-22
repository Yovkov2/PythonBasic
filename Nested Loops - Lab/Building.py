floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    line = ""
    for room in range(rooms):
        if floor == floors:
            line += f"L{floor}{room} "
        elif floor % 2 == 0:
            line += f"O{floor}{room} "
        else:
            line += f"A{floor}{room} "
    print(line.strip())
