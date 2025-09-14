fruit = input()
day = input()
count = float(input())

weekdays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
weekends = {"Saturday", "Sunday"}

weekday_prices = {
    "banana": 2.50, "apple": 1.20, "orange": 0.85, "grapefruit": 1.45,
    "kiwi": 2.70, "pineapple": 5.50, "grapes": 3.85
}
weekend_prices = {
    "banana": 2.70, "apple": 1.25, "orange": 0.90, "grapefruit": 1.60,
    "kiwi": 3.00, "pineapple": 5.60, "grapes": 4.20
}

if day in weekdays:
    prices = weekday_prices
elif day in weekends:
    prices = weekend_prices
else:
    print("error")
    raise SystemExit

if fruit in prices:
    total = count * prices[fruit]
    print(f"{total:.2f}")
else:
    print("error")
