budjet = float(input())
graphic_cards = int(input())
processors = int(input())
ram = int(input())

graphic_cards_sum = graphic_cards * 250
processors_sum = processors * (graphic_cards_sum * 0.35)
ram_sum = ram * (graphic_cards_sum * 0.10)

sum = graphic_cards_sum + processors_sum + ram_sum

if graphic_cards > processors:
    sum *= 0.85

if budjet >= sum:
    print(f"You have {budjet - sum :.2f} leva left!")
else:
    print(f"Not enough money! You need {sum-budjet:.2f} leva more!")