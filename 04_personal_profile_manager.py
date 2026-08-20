first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
fav_color = input("Enter your favorite color: ")
food1 = input("Enter your first favorite food: ")
food2 = input("Enter your second favorite food: ")
food3 = input("Enter your third favorite food: ")

first_name = first_name.capitalize()
last_name = last_name.capitalize()
fav_color = fav_color.capitalize()
food1 = food1.capitalize()
food2 = food2.capitalize()
food3 = food3.capitalize()

full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")
full_name = full_name.upper()
print(f"Full Name (Upper): {full_name}")
full_name = full_name.lower()
print(f"Full Name (Lower): {full_name}")
full_name = full_name.capitalize()
full_name_length = len(full_name)
print(f"Full Name Length: {full_name_length}")

food = [food1, food2, food3]

print(food)
print(food[0])
print(food[2])
print(food[0:2])

food.append("Pasta")
food.insert(1, "Palao")
food.remove("Palao")
food.sort()
food.reverse()

age1 = age + 5
age2 = age + 10
age3 = age * 12

print("Age in 5 years:", age1)
print("Age in 10 years:", age2)
print("Age in months:", age3)
print("Age:", age > 18)
print("Age:", age < 18)
print("Age:", age == 18)
print(f"Name: {full_name}, Age: {age}, Favorite Color: {fav_color}, Favorite Foods: {food}")