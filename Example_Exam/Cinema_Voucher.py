voucher = int(input())

tickets = 0
others = 0

while True:
    purchase = input()
    if purchase == "End":
        break

    price = 0

    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price > voucher:
            break
        tickets += 1
    else:
        price = ord(purchase[0])
        if price > voucher:
            break
        others += 1

    voucher -= price

print(tickets)
print(others)
