while True:
    destination = input()
    if destination == "End":
        break

    needed_budget = float(input())
    saved_money = 0

    while saved_money < needed_budget:
        money = float(input())
        saved_money += money

    print(f"Going to {destination}!")
