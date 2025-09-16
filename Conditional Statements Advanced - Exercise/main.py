sreening_type = input()
rows = int(input())
columns = int(input())

income = 0;

total_sets = rows * columns

if sreening_type == "Premiere":
    income = total_sets * 12
elif sreening_type == "Normal":
    income = total_sets * 7.50
elif sreening_type == "Discount":
    income = total_sets * 5

print(f"{income:.2f} leva")
