numbers = int(input())

musala = monblan = kilimandjaro = k2 = everest = 0
total_people = 0

for _ in range(numbers):
    people = int(input())
    total_people += people

    if people <= 5:
        musala += people
    elif people <= 12:
        monblan += people
    elif people <= 25:
        kilimandjaro += people
    elif people <= 40:
        k2 += people
    else:
        everest += people

print(f"{(musala / total_people) * 100:.2f}%")
print(f"{(monblan / total_people) * 100:.2f}%")
print(f"{(kilimandjaro / total_people) * 100:.2f}%")
print(f"{(k2 / total_people) * 100:.2f}%")
print(f"{(everest / total_people) * 100:.2f}%")
