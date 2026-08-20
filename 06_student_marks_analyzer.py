name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks1 = int(input("Enter your first subject marks: "))
marks2 = int(input("Enter your second subject marks: "))
marks3 = int(input("Enter your third subject marks: "))
marks4 = int(input("Enter your fourth subject marks: "))
marks5 = int(input("Enter your fifth subject marks: "))
fav_subject = input("Enter your favorite subject: ")

name = name.capitalize()
fav_subject = fav_subject.capitalize()

marks = [marks1, marks2, marks3, marks4, marks5]
total_marks = marks1 + marks2 + marks3 + marks4 + marks5

average_marks = total_marks / 5

marks.insert(2, 90)
marks.remove(90)
marks.sort()
marks.reverse()

print("Student Information")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Subject: {fav_subject}")
print(f"Marks: {marks}")
print(f"First Subject Marks: {marks[0]}")
print(f"Last Subject Marks: {marks[-1]}")
print(f"First Three Subjects Marks: {marks[0:3]}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Final Marks List: {marks}")
print(f"Highest Marks: {max(marks)}")
print(f"Lowest Marks: {min(marks)}")
print(f"How many times 80 marks are present: {marks.count(80)}")