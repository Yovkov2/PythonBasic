n = int(input())

total_sales = 0.0
sum_ratings = 0

percent_by_rating = {
    2: 0.00,
    3: 0.50,
    4: 0.70,
    5: 0.85,
    6: 1.00
}
for _ in range(n):
    num = int(input())
    rating = num % 10
    possible_sales = num // 10        #

    sum_ratings += rating
    total_sales += possible_sales * percent_by_rating[rating]

avg_rating = sum_ratings / n

print(f"{total_sales:.2f}")
print(f"{avg_rating:.2f}")