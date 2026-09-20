name = input("Enter your name: ").capitalize()
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))
assignment = input("Assignment is completed? (yes/no): ").lower()

print("Name:", name)
print("Marks:", marks)
print("Attendance:", attendance)
print("Assignment:", assignment)

eligibility_status = "Not Eligible"

if marks >= 90:
    print("Excellent")
    eligibility_status = "Eligible for final exam."

elif marks >= 70:
    print("Good")
    eligibility_status = "Eligible for final exam."

elif marks >= 50:
    print("Passed")

    if attendance >= 75:
        print("Good Attendance")

        if assignment == "yes":
            print("Eligible for final exam.")
            eligibility_status = "Eligible for final exam."
        else:
            print("Complete your assignment first.")

    else:
        print("Not eligible due to low attendance")

else:
    print("Failed")

print("Final Eligibility Status:", eligibility_status)
