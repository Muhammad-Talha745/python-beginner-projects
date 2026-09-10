item = {"Laptop": 50000, "Mobile": 40000, "Watch": 30000, "Mouse": 20000}

need1 = input("Enter Your First Item Name: ").capitalize()
need2 = input("Enter Your Second Item Name: ").capitalize()
need3 = input("Enter Your Third Item Name: ").capitalize()

total = 0

if need1 in item:
    total = total + item[need1]
else:
    print(need1, "is not available")

if need2 in item:
    total = total + item[need2]
else:
    print(need2, "is not available")

if need3 in item:
    total = total + item[need3]
else:
    print(need3, "is not available")

if total > 50000:
    print("You Got 10% Discount")
    discount = total * 0.10
elif total > 25000:
    print("You Got 5% Discount")
    discount = total * 0.05
else:
    print("No Discount")
    discount = 0

final_bill = total - discount

print("\n--- Receipt ---")

if need1 in item:
    print("Item:", need1)
    print("Price:", item[need1])

if need2 in item:
    print("Item:", need2)
    print("Price:", item[need2])

if need3 in item:
    print("Item:", need3)
    print("Price:", item[need3])

print("Total Bill:", total)
print("Discount:", discount)
print("Total Bill After Discount:", final_bill)
