name = input("Enter your name: ")
game1 = input("Enter the name of first game: ")
game2 = input("Enter the name of second game: ")
game3 = input("Enter the name of third game: ")
price1 = int(input("Enter the price of first game: "))
price2 = int(input("Enter the price of second game: "))
price3 = int(input("Enter the price of third game: "))

name = name.capitalize()
game1 = game1.capitalize()
game2 = game2.capitalize()
game3 = game3.capitalize()

games = [game1, game2, game3]
prices = [price1, price2, price3]

total = price1 + price2 + price3
avg = total / 3

print("Customer Name:", name)
print("GAME STORE")
print("Games:")
print(game1, "Rs.", price1)
print(game2, "Rs.", price2)
print(game3, "Rs.", price3)
print("Total:", total)
print("Average:", avg)
print("Most Expensive:", max(prices))
print("Cheapest:", min(prices))

new_game = input("Enter the new game name: ")
new_price = int(input("Enter the price of new game: "))

new_game = new_game.capitalize()
games.append(new_game)
prices.append(new_price)

remove_games = input("Enter the game name that you want to remove: ")

remove_games = remove_games.capitalize()
remove_price = games.index(remove_games)
games.remove(remove_games)
prices.remove(prices[remove_price])

total = prices[0] + prices[1] + prices[2]
avg = total / 3

print("Updated Games:", games)
print("Updated Prices:", prices)
print("Updated Total:", total)
print("Updated Average:", avg)
print("Updated Most Expensive:", max(prices))
print("Updated Cheapest:", min(prices))