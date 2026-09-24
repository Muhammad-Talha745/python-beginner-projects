food1 = input("Enter your first favorite food: ").title()
food2 = input("Enter your second favorite food: ").title()
food3 = input("Enter your third favorite food: ").title()
food4 = input("Enter your fourth favorite food: ").title()
food5 = input("Enter your fifth favorite food: ").title()

fav_foods = (food1, food2, food3, food4, food5)

print("Favorite Foods:", fav_foods)
print("First Food:", fav_foods[0])
print("Last Food:", fav_foods[4])
print("First Three Foods:", fav_foods[0:3])

food1 = input("Enter another food: ").title()
food2 = input("Enter another food: ").title()
food3 = input("Enter another food: ").title()

fav_foods2 = (food1, food2, food3)

final_foods = fav_foods + fav_foods2

print("\nFinal Foods:", final_foods)

search_food = input("\nEnter a food to search: ").title()

print("Food Count:", final_foods.count(search_food))

if search_food in final_foods:
    print("Food Position:", final_foods.index(search_food))
else:
    print("Food not found.")
