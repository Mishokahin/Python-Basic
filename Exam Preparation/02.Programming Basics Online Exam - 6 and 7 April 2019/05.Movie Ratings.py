movie_count = int(input())
highest_rating = 0
lowest_rating = 11
highest_rating_movie = ""
lowest_rating_movie = ""
total_rating = 0

for i in range(movie_count):
    movie_name = input()
    rating = float(input())

    if rating >= highest_rating:
        highest_rating_movie = movie_name
        highest_rating = rating
    if rating <= lowest_rating:
        lowest_rating_movie = movie_name
        lowest_rating = rating

    total_rating += rating

average_rating = total_rating/movie_count
print(f"{highest_rating_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")