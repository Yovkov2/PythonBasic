player_one = int(input())
player_two = int(input())

command = input()
while command != "End":
    if command == "one":
        player_two -= 1
    elif command == "two":
        player_one -= 1

    if player_one == 0:
        print(f"Player one is out of eggs. Player two has {player_two} eggs left.")
        break
    elif player_two == 0:
        print(f"Player two is out of eggs. Player one has {player_one} eggs left.")
        break
    command = input()

if player_one > 0 and player_two > 0:
    print(f"Player one has {player_one} eggs left.")
    print(f"Player two has {player_two} eggs left.")