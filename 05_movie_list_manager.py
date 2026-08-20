movie1 = input("Enter the name of your first favorite movie: ")
movie2 = input("Enter the name of your second favorite movie: ")
movie3 = input("Enter the name of your third favorite movie: ")
movie4 = input("Enter the name of your fourth favorite movie: ")
movie5 = input("Enter the name of your fifth favorite movie: ")
movies = [movie1, movie2, movie3, movie4, movie5]

print(movies)
print(movies[0])
print(movies[4])
print(movies[0:3])

movies.append("The Matrix")
movies.insert(1, "Inception")
movies.remove("The Matrix")
movies.reverse()
movies.sort()

print(movies)
print(movies.count("Inception"))
print(movies.index("Inception"))

more_movies = ["The Godfather", "Pulp Fiction", "The Dark Knight"]
movies.extend(more_movies)

print(movies)