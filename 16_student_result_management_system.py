number_of_students = int(input("Enter number of students: "))

students = []
student_number = 0

while student_number < number_of_students:
    print(f"\n===== STUDENT {student_number + 1} =====")

    name = input("Enter student name: ").title()

    math = int(input("Enter Math marks: "))
    english = int(input("Enter English marks: "))
    science = int(input("Enter Science marks: "))

    marks = [math, english, science]
    subjects = ["Math", "English", "Science"]

    student_number = student_number + 1

    total = 0
    count = 0
    highest = marks[0]
    lowest = marks[0]
    passed = 0
    failed = 0
    below_40 = 0

    for i in range(3):
        mark = marks[i]
        subject = subjects[i]

        total = total + mark
        count = count + 1

        if mark >= 50:
            passed = passed + 1
            print(f"{subject}: Passed")
        else:
            failed = failed + 1
            print(f"{subject}: Failed")

        if mark < 40:
            below_40 = below_40 + 1

        if mark > highest:
            highest = mark

        if mark < lowest:
            lowest = mark

    average = total / count

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if average >= 50:
        if below_40 == 0:
            result = "Passed"
        else:
            result = "Failed"
    else:
        result = "Failed"

    student = {
        "Name": name,
        "Total": total,
        "Average": average,
        "Highest": highest,
        "Lowest": lowest,
        "Passed Subjects": passed,
        "Failed Subjects": failed,
        "Grade": grade,
        "Result": result,
    }

    students.append(student)


print("\n===== STUDENT RESULTS =====")

for student in students:
    print("\nName:", student["Name"])
    print("Total:", student["Total"])
    print("Average:", student["Average"])
    print("Highest:", student["Highest"])
    print("Lowest:", student["Lowest"])
    print("Passed Subjects:", student["Passed Subjects"])
    print("Failed Subjects:", student["Failed Subjects"])
    print("Grade:", student["Grade"])
    print("Result:", student["Result"])


passed_students = 0
failed_students = 0

for student in students:
    if student["Result"] == "Passed":
        passed_students = passed_students + 1
    else:
        failed_students = failed_students + 1


class_total = 0
student_count = 0

for student in students:
    class_total = class_total + student["Average"]
    student_count = student_count + 1

class_average = class_total / student_count


highest_average = students[0]["Average"]

for student in students:
    if student["Average"] > highest_average:
        highest_average = student["Average"]


lowest_average = students[0]["Average"]

for student in students:
    if student["Average"] < lowest_average:
        lowest_average = student["Average"]

print("\n===== CLASS STATISTICS =====")
print("Total Students:", student_count)
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print("Class Average:", class_average)
print("Highest Student Average:", highest_average)
print("Lowest Student Average:", lowest_average)
