fav_movies = ["Avenger's: Endgame", "Iron Man", "Cast Away", "Black Hawk Down", "Star Wars: Return of the Jedi"]

print(f"The list fav_movies includes my top {len(fav_movies)} favorite movies")
print(fav_movies)

#4a sorted() method. I noticed that the function sorted the list alphabetically.
print(sorted(fav_movies))
print(fav_movies)

#4b .sort() method. I noticed that the .sort() function permanently sorts the list.
fav_movies.sort()
print(fav_movies)

#5 
fav_movies.append("Captain America and The Winter Soldier")
print(fav_movies)
print(f"Included {fav_movies[len(fav_movies)-1]} to fav_movies")
