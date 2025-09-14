type_animal = input()
result = ""

if type_animal == "dog":
    result = "mammal"
elif type_animal == "crocodile" or type_animal == "tortoise" or type_animal == "snake":
    result = "reptile"
else:
    result = "unknown"

print(result)