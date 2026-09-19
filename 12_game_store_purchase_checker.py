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
    purchase_status = "Purchase Successful"
    remaining_balance = ava_bal - final_price

elif ava_bal >= final_price - 5000:
    purchase_status = "Insufficient Balance"
    remaining_balance = ava_bal

else:
    purchase_status = "Balance Too Low"
    remaining_balance = ava_bal

print(f"Game: {game}")
print(f"Discount: {discount}")
print(f"Final Price: {final_price}")
print(f"Remaining Balance: {remaining_balance}")
print(f"Purchase Status: {purchase_status}")
