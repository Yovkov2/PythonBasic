naylon = float(input()) + 2
paint = (float(input()) * 1.10) * 14.50
separators = float(input()) * 5
hours = float(input())

naylon *= 1.50


sumMaterials = naylon + paint + separators + 0.40
master = (sumMaterials * 0.30) * hours
sum = sumMaterials + master

print(sum)