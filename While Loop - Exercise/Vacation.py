price_vacation = float(input())
money_have = float(input())
days = 0
counter_spent = 0

while True:
    command = input()
    money = float(input())
    days += 1

    if command == "spend":
        counter_spent += 1
        money_have -= money
        if money_have < 0:
            money_have = 0
        if counter_spent == 5:
            print("You can't save the money.")
            print(days)
            break
    elif command == "save":
        money_have += money
        counter_spent = 0
        if money_have >= price_vacation:
            print(f"You saved the money for {days} days.")
            break

