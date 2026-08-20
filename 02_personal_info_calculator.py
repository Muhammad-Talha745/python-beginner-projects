name = input("Enter your full name: ")
age = int(input("Enter your age: "))
fav_num = int(input("Enter your favourite number: "))

name = name.upper()

is_name = name.isdigit()

age_5 = age + 5

fav_num_half = fav_num / 2
fav_num_floor_half = fav_num // 2

age_fav_num = age >= 18 and fav_num > 10

print(
    f"My name is {name} (is all digits: {is_name}), I am {age} years old, "
    f"and in five years I will be {age_5} years old, and my favourite number "
    f"is {fav_num}. Half of my favourite number is {fav_num_half} "
    f"(normal division) and {fav_num_floor_half} (floor division)."
)

print(f"Age is 18 or older and favourite number is greater than 10: {age_fav_num}")