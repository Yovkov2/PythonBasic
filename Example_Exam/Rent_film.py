rent = int(input())

statuets = rent * 0.70
ceturing = statuets * 0.85
volume = ceturing / 2
sum = rent + statuets + ceturing + volume

print(f"{sum:.2f}")