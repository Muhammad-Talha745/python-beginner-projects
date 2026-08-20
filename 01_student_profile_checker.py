name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
fav_language = input("Enter your favorite programming language: ")
marks = int(input("Enter your marks (out of 100): "))

name = name.capitalize()
country = country.capitalize()
fav_language = fav_language.capitalize()

print(
    f"My name is {name} and I am {age} years old. "
    f"I am from {country} and my favorite programming language is {fav_language}."
)
print(f"After 5 bonus marks, my total marks will be {marks + 5}.")
print(f"Marks greater than 50: {marks > 50}")
print(f"Marks less than 50: {marks < 50}")
print(f"Marks equal to 50: {marks == 50}")