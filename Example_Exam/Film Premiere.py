film = input()
product = input()
count_bilet = int(input())
total_sum = 0

if film == "John Wick":
    if product == "Drink":
        total_sum = count_bilet * 12
    elif product == "Popcorn":
        total_sum = count_bilet * 15
    elif product == "Menu":
        total_sum = count_bilet * 19
elif film == "Star Wars":
    if product == "Drink":
        total_sum = count_bilet * 18
    elif product == "Popcorn":
        total_sum = count_bilet * 25
    elif product == "Menu":
        total_sum = count_bilet * 30
    if count_bilet >= 4:  
        total_sum *= 0.70
elif film == "Jumanji":
    if product == "Drink":
        total_sum = count_bilet * 9
    elif product == "Popcorn":
        total_sum = count_bilet * 11
    elif product == "Menu":
        total_sum = count_bilet * 14
    if count_bilet == 2:
        total_sum *= 0.85

print(f"Your bill is {total_sum:.2f} leva.")