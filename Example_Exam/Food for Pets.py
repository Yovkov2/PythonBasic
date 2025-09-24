days = int(input())
total_food = float(input())

dog_total = 0
cat_total = 0
biscuits = 0

for day in range(1, days + 1):
    dog_eaten = int(input())
    cat_eaten = int(input())

    dog_total += dog_eaten
    cat_total += cat_eaten

    if day % 3 == 0:
        biscuits += 0.10 * (dog_eaten + cat_eaten)

total_eaten = dog_total + cat_total
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_eaten / total_food * 100:.2f}% of the food has been eaten.")
print(f"{dog_total / total_eaten * 100:.2f}% eaten from the dog.")
print(f"{cat_total / total_eaten * 100:.2f}% eaten from the cat.")