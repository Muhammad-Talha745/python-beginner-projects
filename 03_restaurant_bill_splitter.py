rest_name = input("Enter the restaurant name: ")
tot_bill = float(input("Enter the total bill amount before tip: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
tot_people = int(input("Enter the total number of people splitting the bill: "))

rest_name = rest_name.title()
tip_amount = tot_bill * (tip_percentage / 100)
total_bill = tot_bill + tip_amount
per_person = total_bill / tot_people
whole_per_person = total_bill // tot_people
is_large_group_or_big_bill = tot_people >= 5 or total_bill > 100

print(f"Restaurant Name: {rest_name}")
print(f"Total Bill: ${tot_bill:.2f}")
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total Bill with Tip: ${total_bill:.2f}")
print(f"Amount per Person: ${per_person:.2f}")
print(f"Whole Dollar Amount per Person: ${whole_per_person:.0f}")
print(f"Is Large Group or Big Bill: {is_large_group_or_big_bill}")