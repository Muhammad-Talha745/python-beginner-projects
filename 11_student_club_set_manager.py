python_member1 = input("Enter Python Club member 1: ").title()
python_member2 = input("Enter Python Club member 2: ").title()
python_member3 = input("Enter Python Club member 3: ").title()
python_member4 = input("Enter Python Club member 4: ").title()
python_member5 = input("Enter Python Club member 5: ").title()

python_club = {
    python_member1,
    python_member2,
    python_member3,
    python_member4,
    python_member5,
}

ai_member1 = input("Enter AI Club member 1: ").title()
ai_member2 = input("Enter AI Club member 2: ").title()
ai_member3 = input("Enter AI Club member 3: ").title()
ai_member4 = input("Enter AI Club member 4: ").title()

ai_club = {ai_member1, ai_member2, ai_member3, ai_member4}

print("Python Club:", python_club)
print("AI Club:", ai_club)
print("Python Club Members:", len(python_club))
print("AI Club Members:", len(ai_club))

new_member = input("Enter a new Python Club member: ").title()

python_club.add(new_member)

remove_member = input("Enter a Python Club member to remove: ").title()

if remove_member in python_club:
    python_club.remove(remove_member)

print("Updated Python Club:", python_club)

search_member = input("Enter a member to check: ").title()

print("Is member in Python Club:", search_member in python_club)

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

small_member1 = input("\nEnter a member for the small set: ").title()
small_member2 = input("Enter another member for the small set: ").title()

small_set = {small_member1, small_member2}

print("Small Set Is Subset:", small_set.issubset(ai_club))
print("AI Club Is Superset:", ai_club.issuperset(small_set))

common_member_count = 0

for member in common_members:
    common_member_count = common_member_count + 1

print("Number of Common Members:", common_member_count)
