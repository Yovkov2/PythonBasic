prime_sum = 0
nonprime_sum = 0

while True:
    command = input()
    if command == "stop":
        break

    number = int(command)

    if number < 0:
        print("Number is negative.")
        continue

    # check if prime
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        prime_sum += number
    else:
        nonprime_sum += number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {nonprime_sum}")
