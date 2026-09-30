students = {
    "Ravi": [85, 78, 90],
    "Sita": [65, 72, 68],
    "Rahul": [92, 88, 95],
    "Priya": [55, 61, 58],
    "Arun": [75, 80, 70]
}

all_marks = []

for name, marks in students.items():

    total = sum(marks)
    average = total / len(marks)

    all_marks.extend(marks)

    print("Student:", name)
    print("Total:", total)
    print("Average:", average)

    if average >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

    print("----------------")

print("Highest Mark:", max(all_marks))
print("Lowest Mark:", min(all_marks))
