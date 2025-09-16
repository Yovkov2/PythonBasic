budjet = float(input())
season = input()

if budjet <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        budjet *= 0.30
        print(f"Camp - {budjet:.2f}")
    elif season == "winter":
        budjet *= 0.70
        print(f"Hotel - {budjet:.2f}")
elif budjet <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        budjet *= 0.40
        print(f"Camp - {budjet:.2f}")
    elif season == "winter":
        budjet *= 0.80
        print(f"Hotel - {budjet:.2f}")
elif budjet > 1000:
    print("Somewhere in Europe")
    budjet *= 0.90
    print(f"Hotel - {budjet:.2f}")