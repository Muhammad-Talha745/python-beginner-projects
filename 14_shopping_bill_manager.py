item = {"Laptop": 50000, "Mobile": 40000, "Watch": 30000, "Mouse": 20000}

need1 = input("Enter Your First Item Name: ").capitalize()
need2 = input("Enter Your Second Item Name: ").capitalize()
need3 = input("Enter Your Third Item Name: ").capitalize()

total = 0

selected_items = []

if need1 in item:
    total = total + item[need1]
    selected_items.append(need1)
else:
    print(need1, "is not available")

if need2 in item:
    total = total + item[need2]
    selected_items.append(need2)
else:
    print(need2, "is not available")

if need3 in item:
    total = total + item[need3]
    selected_items.append(need3)
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
expensive_items = 0

for selected_item in selected_items:
    if item[selected_item] >= 30000:
        expensive_items = expensive_items + 1

print("\n--- Receipt ---")

for selected_item in selected_items:
    print("Item:", selected_item)
    print("Price:", item[selected_item])


print("Total Bill:", total)
print("Discount:", discount)
print("Total Bill After Discount:", final_bill)
print("Items Rs. 30,000 or More:", expensive_items)
