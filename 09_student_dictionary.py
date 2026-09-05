name = input("Enter your name:")
age = int(input("Enter your age:"))
fav_sub = input("Enter your favorite subject:")

name = name.capitalize()
fav_sub = fav_sub.capitalize()

student = { 'name' : name,  'age' : age, 'fav_sub' : fav_sub }

print(student)
print(student["name"])

student["age"] = age + 1

country = input("Enter your country name:")

country = country.capitalize()

student["country"] = country

print(student)