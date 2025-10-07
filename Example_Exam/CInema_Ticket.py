total_tickets = 0
student = 0
standard = 0
kid = 0
while True:
    movie = input()
    if movie == "Finish":
        break

    free_seats = int(input())
    sold_this = 0

    while sold_this < free_seats:
        ticket_type = input()
        if ticket_type == "End":
            break

        sold_this += 1
        total_tickets += 1

        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1

    print(f"{movie} - {sold_this / free_seats * 100:.2f}% full.")

print(f"Total tickets: {total_tickets}")
if total_tickets > 0:
    print(f"{student / total_tickets * 100:.2f}% student tickets.")
    print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
    print(f"{kid / total_tickets * 100:.2f}% kids tickets.")
else:
    print("0.00% student tickets.")
    print("0.00% standard tickets.")
    print("0.00% kids tickets.")