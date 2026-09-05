python_club = {"Ali", "Ahmed", "Sara", "Hamza", "Ali"}
ai_club = {"Sara", "Hamza", "Usman", "Ayesha"}

print(python_club)
print(ai_club)

print(len(python_club))
print(len(ai_club))

python_club.add("Bilal")
python_club.remove("Ahmed")
print(python_club)

print("Sara" in python_club)

print(python_club.union(ai_club))
print(python_club.intersection(ai_club))
print(python_club.difference(ai_club))
print(python_club.symmetric_difference(ai_club))

python_copy = python_club.copy()
python_copy.difference_update(ai_club)
print(python_copy)

python_copy = python_club.copy()
python_copy.intersection_update(ai_club)
print(python_copy)

print(python_club.isdisjoint(ai_club))

small_set = {"Sara", "Hamza"}

print(small_set.issubset(ai_club))
print(ai_club.issuperset(small_set))
