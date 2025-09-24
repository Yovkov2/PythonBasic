start = input()
end = input()

for d1 in range(int(start[0]), int(end[0]) + 1):
    for d2 in range(int(start[1]), int(end[1]) + 1):
        for d3 in range(int(start[2]), int(end[2]) + 1):
            for d4 in range(int(start[3]), int(end[3]) + 1):
                if d1 % 2 != 0 and d2 % 2 != 0 and d3 % 2 != 0 and d4 % 2 != 0:
                    print(f"{d1}{d2}{d3}{d4}", end=" ")