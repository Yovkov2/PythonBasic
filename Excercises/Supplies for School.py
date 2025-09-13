pens = float(input()) * 5.80
markers = float(input()) * 7.20
preparats = float(input()) * 1.20
precent = float(input())

sum = pens + markers + preparats
print(sum - (sum*precent)/100)
