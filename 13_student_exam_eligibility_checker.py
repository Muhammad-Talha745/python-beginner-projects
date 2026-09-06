name = input("Enter your name:").capitalize()
marks = int(input("Enter your marks:"))
attendance = int(input("Enter your attendance percentage:"))
assignment = input("Assignment is completed? (yes/no):").lower()

print("Name:", name)
print("Marks", marks)
print("Attendance:", attendance)
print("Assignment:", assignment)

if marks >= 90:
    print("Excellent")

elif marks >= 70:
    print("Good")

elif marks >= 50:
    print("Passed")

    if attendance >= 75:
        print("Good Attendance")

        if assignment == "yes":
            print("Eligible for final exam.")
        else:
            print("Complete your assignment first.")

    else:
        print("Not eligible due to low attendance")

else:
    print("Failed")
