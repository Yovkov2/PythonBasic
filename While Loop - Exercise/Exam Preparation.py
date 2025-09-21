max_poor_grades = int(input())
poor_grades_count = 0
grades_sum = 0
task_counter = 0
last_problem = ""

while True:
    task_name = input()
    if task_name == "Enough":
        average = grades_sum / task_counter
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {task_counter}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    grades_sum += grade
    task_counter += 1
    last_problem = task_name
    if grade <= 4:
        poor_grades_count += 1
        if poor_grades_count >= max_poor_grades:
            print(f"You need a break, {poor_grades_count} poor grades.")
            break