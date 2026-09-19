python_club = {"Ali", "Ahmed", "Sara", "Hamza", "Ali"}

ai_club = {"Sara", "Hamza", "Usman", "Ayesha"}

print(python_club)
print(ai_club)

print("Python Club Members:", len(python_club))
print("AI Club Members:", len(ai_club))

python_club.add("Bilal")

python_club.remove("Ahmed")

print("Updated Python Club:", python_club)

print("Is Sara in Python Club:", "Sara" in python_club)

common_members = python_club.intersection(ai_club)

print("Union:", python_club.union(ai_club))
print("Common Members:", common_members)
print("Python Club Only:", python_club.difference(ai_club))
print("Members in Only One Club:", python_club.symmetric_difference(ai_club))

python_copy = python_club.copy()

python_copy.difference_update(ai_club)

print("Python Club Copy After Difference Update:", python_copy)

python_copy = python_club.copy()

python_copy.intersection_update(ai_club)

print("Python Club Copy After Intersection Update:", python_copy)

print("Are Clubs Disjoint:", python_club.isdisjoint(ai_club))

small_set = {"Sara", "Hamza"}

print("Small Set Is Subset:", small_set.issubset(ai_club))

print("AI Club Is Superset:", ai_club.issuperset(small_set))

common_member_count = 0

for member in common_members:
    common_member_count = common_member_count + 1

print("Number of Common Members:", common_member_count)
