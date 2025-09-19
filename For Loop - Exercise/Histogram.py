numbers = int(input())
p1 = p2 = p3 = p4 = p5 = 0

for i in range(1, numbers + 1):
    new_number = int(input())
    if new_number < 200:
        p1 += 1
    elif new_number >= 200 and new_number <= 399:
        p2 += 1
    elif new_number >= 400 and new_number <= 599:
        p3 += 1
    elif new_number >= 600 and new_number <= 799:
        p4 += 1
    elif new_number >= 800:
        p5 += 1

print(f"{(p1 / numbers) * 100:.2f}%")
print(f"{(p2 / numbers) * 100:.2f}%")
print(f"{(p3 / numbers) * 100:.2f}%")
print(f"{(p4 / numbers) * 100:.2f}%")
print(f"{(p5 / numbers) * 100:.2f}%")