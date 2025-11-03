maznini = int(input())
protein = int(input())
vuglehidrat = int(input())
calories = int(input())
water = int(input())

sum_maznini = (calories * (maznini / 100)) / 9
sum_protein = (calories * (protein / 100)) / 4
sum_vuglehidrat = (calories * (vuglehidrat / 100)) / 4

total_food_weight = sum_maznini + sum_protein + sum_vuglehidrat

calories_per_gram = calories / total_food_weight

calories_per_gram_without_water = calories_per_gram * (1 - (water / 100))

print(f"{calories_per_gram_without_water:.4f}")