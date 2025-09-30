target = int(input())

bar = target - 30
total_jumps = 0
last_cleared = 0

while bar <= target:
    fails_on_this_bar = 0


    while fails_on_this_bar < 3:
        jump = int(input())
        total_jumps += 1

        if jump > bar:
            last_cleared = bar
            bar += 5
            break
        else:
            fails_on_this_bar += 1

    if fails_on_this_bar == 3:
        print(f"Tihomir failed at {bar}cm after {total_jumps} jumps.")
        exit()

print(f"Tihomir succeeded, he jumped over {last_cleared}cm after {total_jumps} jumps.")
