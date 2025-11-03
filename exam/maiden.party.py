maiden_money = float(input())
love_message = int(input())
love_rosses = int(input())
love_keys = int(input())
love_image = int(input())
love_surprise = int(input())

total_sum = love_message * 0.60 + love_rosses * 7.20 + love_keys * 3.60 + love_image * 18.20 + love_surprise * 22
total_count = love_message + love_rosses + love_keys + love_image + love_surprise
if total_count >= 25:
    total_sum *= 0.65

total_sum *= 0.90

if total_sum >= maiden_money:
    money_left = total_sum - maiden_money
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = maiden_money - total_sum
    print(f"Not enough money! {money_needed:.2f} lv needed.")