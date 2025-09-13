deposit = float(input())
months = int(input())
precent = float(input())

interest = deposit * precent/100
interestForMonth = interest/12
sum = deposit + months * interestForMonth

print(sum)