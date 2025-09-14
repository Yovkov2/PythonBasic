import sys

city = input()
salary = float(input())
sum = 0

if city == "Sofia":
   if salary < 0:
       print("error")
       sys.exit()
   elif salary <= 500:
       sum = salary * 0.05
   elif salary <= 1000:
       sum = salary * 0.07
   elif salary <= 10000:
       sum = salary * 0.08
   else:
       sum = salary * 0.12

elif city == "Varna":
   if salary < 0:
       print("error")
       sys.exit()
   elif salary <= 500:
       sum = salary * 0.045
   elif salary <= 1000:
       sum = salary * 0.075
   elif salary <= 10000:
       sum = salary * 0.10
   else:
       sum = salary * 0.13

elif city == "Plovdiv":
   if salary < 0:
       print("error")
       sys.exit()
   elif salary <= 500:
       sum = salary * 0.055
   elif salary <= 1000:
       sum = salary * 0.08
   elif salary <= 10000:
       sum = salary * 0.12
   else:
       sum = salary * 0.145

else:
    print("error")
    sys.exit()

print(f"{sum:.2f}")
