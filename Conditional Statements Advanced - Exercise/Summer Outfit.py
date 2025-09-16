degree = int(input())
type_day = input()

outfit = ""
shoes = ""

if degree >= 10 and degree <= 18:
    if type_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif type_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif type_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degree > 18 and degree <= 24:
    if type_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif type_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif type_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degree > 24:
    if type_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif type_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif type_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")