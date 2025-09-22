n = int(input())

total_sum = 0
presentations_count = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break

    current_sum = 0
    for _ in range(n):
        grade = float(input())
        current_sum += grade

    avg_grade = current_sum / n
    print(f"{presentation} - {avg_grade:.2f}.")

    total_sum += avg_grade
    presentations_count += 1

final_assessment = total_sum / presentations_count
print(f"Student's final assessment is {final_assessment:.2f}.")
