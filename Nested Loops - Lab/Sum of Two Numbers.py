start = int(input())
end = int(input())
magic = int(input())

combination = 0
found = False

for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        combination += 1
        if x1 + x2 == magic:
            print(f"Combination N:{combination} ({x1} + {x2} = {magic})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{combination} combinations - neither equals {magic}")
