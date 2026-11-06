students = {"Talha": 5000, "Haseeb": 4000, "Ahsan": 3000}

print("===== STUDENT INFORMATION =====")

for student_name, monthly_allowance in students.items():
    print(f"Name: {student_name}")
    print(f"Monthly Allowance: {monthly_allowance}")


def calculate_total(allowances):
    total = 0

    for allowance in allowances:
        total = total + allowance

    return total


def calculate_average(total, number_of_students):
    average = total / number_of_students
    return average


def calculate_savings(allowance, expense):
    savings = allowance - expense
    return savings


allowances = [5000, 4000, 3000]

total_allowance = calculate_total(allowances)

number_of_students = 3

average_allowance = calculate_average(total_allowance, number_of_students)

talha_allowance = students["Talha"]

monthly_expenses = int(input("\nEnter Talha's monthly expenses: "))

remaining_savings = calculate_savings(talha_allowance, monthly_expenses)

print("\n===== STUDENT FINANCE REPORT =====")

print("Total Students:", number_of_students)
print("Total Class Allowance:", total_allowance)
print("Average Allowance:", average_allowance)

print("\n===== TALHA'S FINANCIAL DETAILS =====")

print("Student Name: Talha")
print("Monthly Allowance:", talha_allowance)
print("Monthly Expenses:", monthly_expenses)
print("Remaining Savings:", remaining_savings)
