first_player = input()
second_player = input()
sum_first = 0
sum_second = 0

command = input()
while command != "End of game":
    first_card = int(command)
    second_card = int(input())
    if first_card > second_card:
        sum_first += first_card - second_card
    elif second_card > first_card:
        sum_second += second_card - first_card
    else:
        print("Number wars!")
        first_war_card = int(input())
        second_war_card = int(input())
        if first_war_card > second_war_card:
            print(f"{first_player} is winner with {sum_first} points")
        else:
            print(f"{second_player} is winner with {sum_second} points")
        break
    command = input()

if command == "End of game":
    print(f"{first_player} has {sum_first} points")
    print(f"{second_player} has {sum_second} points")