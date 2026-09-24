students = {"Ali": 78, "Ahmed": 92, "Sara": 65, "Hassan": 45, "Ayesha": 88}

passed_students = []
failed_students = []

for student_key, student_value in students.items():
    if student_value >= 50:
        passed_students.append(student_key)
        result = "Passed"
    else:
        failed_students.append(student_key)
        result = "Failed"
    if student_value >= 90:
        grade = "A+"
    elif student_value >= 80:
        grade = "A"
    elif student_value >= 70:
        grade = "B"
    elif student_value >= 60:
        grade = "C"
    elif student_value >= 50:
        grade = "D"
    else:
        grade = "F"
    if student_value % 2 == 0:
        number_type = "Even"
    else:
        number_type = "Odd"

    print(
        student_key,
        "| Marks:",
        student_value,
        "|",
        result,
        "| Grade:",
        grade,
        "|",
        number_type,
    )

total = 0
count = 0

for student_value in students.values():
    total = total + student_value
    count = count + 1

avg = total / count

if avg >= 50:
    class_result = "Class Passed"
else:
    class_result = "Class Failed"

result = ("Passed", "Failed")
passed_result, failed_result = result

print("\n===== CLASS SUMMARY =====")
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print("Total Marks:", total)
print("Class Average:", avg)
print("Class Result:", class_result)
