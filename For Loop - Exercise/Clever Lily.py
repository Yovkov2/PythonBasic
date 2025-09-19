age = int(input())
washer_machine = float(input())
toy_money = int(input())
constantsa = 1
sum = 0

for i in range(1, age + 1):
    if i % 2 == 1:
        sum += toy_money
    else:
        sum += constantsa * 10
        sum -= 1
        constantsa += 1

if sum >= washer_machine:
    print(f"Yes! {sum - washer_machine:.2f}")
else:
    print(f"No! {washer_machine - sum:.2f}")