name = input()
seasons = int(input())
episode = int(input())
time = float(input())

add_time = time * 0.20
total_time = time + add_time
add_special_episode = seasons * 10
sum = total_time * episode * seasons + add_special_episode
print(f"Total time needed to watch the {name} series is {int(sum)} minutes.")