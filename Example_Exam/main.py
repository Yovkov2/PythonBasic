strawberry_price = float(input())
bananas_count = float(input())
oranges_count = float(input())
raspberries_count = float(input())
strawberries_count = float(input())

raspberries_price = strawberry_price / 2
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

raspberries_sum = raspberries_count * raspberries_price
oranges_sum = oranges_count * oranges_price
bananas_sum = bananas_count * bananas_price
strawberries_sum = strawberries_count * strawberry_price

total = raspberries_sum + oranges_sum + bananas_sum + strawberries_sum
print(f"{total:.2f}")
