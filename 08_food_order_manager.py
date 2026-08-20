name = input("Enter your name: ")
food1 = input("Enter the name of first food you ordered: ")
food2 = input("Enter the name of second food you ordered: ")
food3 = input("Enter the name of third food you ordered: ")
price1 = int(input("Enter the price of first food you ordered: "))
price2 = int(input("Enter the price of second food you ordered: "))
price3 = int(input("Enter the price of third food you ordered: "))

name = name.capitalize()
food1 = food1.capitalize()
food2 = food2.capitalize()
food3 = food3.capitalize()

foods = [food1, food2, food3]
prices = [price1, price2, price3]

total = price1 + price2 + price3
avg = total / 3

print("RECEIPT")
print("Name:", name)
print(food1, "Rs.", price1)
print(food2, "Rs.", price2)
print(food3, "Rs.", price3)
print("Total Bill:", total)
print("Average Item Price:", avg)
print("Most Expensive:", max(prices))
print("Cheapest:", min(prices))

new_food = input("Enter the name of new food: ")
new_price = int(input("Enter the price of new food: "))

new_food = new_food.capitalize()
foods.append(new_food)
prices.append(new_price)

rem_food = input("Enter the name of food that you don't want: ")

rem_food = rem_food.capitalize()
rem_price = foods.index(rem_food)
foods.remove(rem_food)
prices.remove(prices[rem_price])

total_u = prices[0] + prices[1] + prices[2]
avg_u = total_u / 3

print("Updated Foods:", foods)
print("Updated Prices:", prices)
print("Updated Total:", total_u)
print("Updated Average:", avg_u)
print("Updated Most Expensive:", max(prices))
print("Updated Cheapest:", min(prices))