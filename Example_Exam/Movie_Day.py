time_photos = int(input())
count_scene = int(input())
time_scene = int(input())

teren = time_photos * 0.15
time_scenes = count_scene * time_scene
total_time = teren + time_scenes
if time_photos >= total_time:
    print(f"You managed to finish the movie on time! You have {int(time_photos - total_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {int(total_time - time_photos)} minutes.")