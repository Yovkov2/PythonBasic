tokens = int(input())
bonus = 0

if tokens <= 100:
    bonus +=5
elif tokens > 100 and tokens <= 1000:
    bonus = tokens * 0.2
else:
    bonus = tokens * 0.1

if tokens % 2 == 0:
    bonus+=1
if tokens % 10 == 5:
    bonus += 2

print(bonus)
print(tokens + bonus)