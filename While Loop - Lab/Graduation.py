name = input()
current_grade = 1
failures = 0
total_score = 0

while current_grade <= 12:
    annual_score = float(input())

    if annual_score < 4.00:
        failures += 1
        if failures > 1:
            print(f"{name} has been excluded at {current_grade} grade")
            break

        continue

    total_score += annual_score
    current_grade += 1

else:
    average = total_score / 12
    print(f"{name} graduated. Average grade: {average:.2f}")