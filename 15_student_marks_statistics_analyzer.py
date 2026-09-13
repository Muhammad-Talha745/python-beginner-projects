marks = [78, 45, 92, 61, 88, 35, 70]

total = 0
student_count = 0
passed = 0

highest_mark = marks[0]
lowest_mark = marks[0]
second_highest_mark = marks[0]

for mark in marks:
    student_count = student_count + 1
    total = total + mark

    if mark >= 50:
        passed = passed + 1

    if mark < lowest_mark:
        lowest_mark = mark

    if mark > highest_mark:
        second_highest_mark = highest_mark
        highest_mark = mark

    elif mark > second_highest_mark and mark != highest_mark:
        second_highest_mark = mark


average = total / student_count

above_average = 0
below_average = 0
seventy_or_above = 0

for mark in marks:
    if mark > average:
        above_average = above_average + 1

    if mark < average:
        below_average = below_average + 1

    if mark >= 70:
        seventy_or_above = seventy_or_above + 1


print("Total:", total)
print("Passed:", passed)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Average:", average)
print("Above Average:", above_average)
print("Second Highest:", second_highest_mark)
print("Below Average:", below_average)
print("70 or Above:", seventy_or_above)
