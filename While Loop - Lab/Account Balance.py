command = input()
sum = 0

while command != "NoMoreMoney":
    money = float(command)
    if money < 0:
        print("Invalid operation!")
        break
    sum += money
    print(f"Increase: {money:.2f}")
    command = input()

print(f"Total: {sum:.2f}")