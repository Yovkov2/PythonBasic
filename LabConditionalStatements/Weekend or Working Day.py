work_bench = input()
result = ""

if work_bench == "Monday" or work_bench == "Tuesday" or work_bench == "Wednesday" or work_bench == "Thursday" or work_bench == "Friday":
    result = "Working day"
elif work_bench == "Saturday" or work_bench == "Sunday":
    result = "Weekend"
else:
    result = "Error"

print(result)