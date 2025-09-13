lenth = int(input())
width = int(input())
height = int(input())
precent = float(input())

sumArea = lenth * width * height
sumLitllres = sumArea * 0.001
sum = sumLitllres * (1-precent/100)
print(sum)