result = input()
result2 = input()
result3 = input()

sum_win = 0
sum_lost = 0
sum_draw = 0

if result[0] > result[2]:
    sum_win+=1
elif result[2] > result[0]:
    sum_lost+=1
elif result[0] == result[2]:
    sum_draw += 1
if result2[0] > result2[2]:
    sum_win+=1
elif result2[2] > result2[0]:
    sum_lost+=1
elif result2[0] == result2[2]:
    sum_draw += 1
if result3[0] > result3[2]:
    sum_win+=1
elif result3[2] > result3[0]:
    sum_lost+=1
elif result3[0] == result3[2]:
    sum_draw += 1

print(f"Team won {sum_win} games.")
print(f"Team lost {sum_lost} games.")
print(f"Drawn games: {sum_draw}")