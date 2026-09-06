name = input("Customer Name: ").capitalize()
game = input("Game Name: ").capitalize()
price = int(input("Game price: "))
ava_bal = int(input("Available balance: "))
membership = input("Membership? (yes/no): ").lower()

discount = 0

print(f"Customer Name: {name}")
print(f"Game Name: {game}")
print(f"Game Price: {price}")
print(f"Available Balance: {ava_bal}")
print(f"Membership: {membership}")

if membership == "yes":
    print("20% Discount")
    discount = price * 20 / 100
    final_price = price - discount
else:
    print("No Discount")
    final_price = price

if ava_bal >= final_price:
    print("Purchase Successful")
    remaining_balance = ava_bal - final_price
else:
    print("Cannot afford the game")
    remaining_balance = ava_bal

print(f"Game: {game}")
print(f"Discount: {discount}")
print(f"Final Price: {final_price}")
print(f"Remaining Balance: {remaining_balance}")
