count_film = int(input())

total_rating = 0

max_film = ""
max_rating = float('-inf')

min_film = ""
min_rating = float('inf')

for i in range(count_film):
    film_name = input()
    rating = float(input())

    total_rating += rating

    if rating > max_rating:
        max_rating = rating
        max_film = film_name

    if rating < min_rating:
        min_rating = rating
        min_film = film_name

average_rating = total_rating / count_film

print(f"{max_film} is with highest rating: {max_rating:.1f}")
print(f"{min_film} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
