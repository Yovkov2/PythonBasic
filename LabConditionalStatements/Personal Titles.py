age = float(input())
gender = input()
result = ""

if age >= 16:
    if gender == "m":
        result = "Mr."
    elif gender == "f":
        result = "Ms."
elif age <= 16:
    if gender == "m":
        result = "Master"
    elif gender == "f":
        result = "Miss"

print(result)