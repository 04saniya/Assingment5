student_marks = {  "Saniya": 85,
    "Keerti": 92,
    "Rahul": 78,
    "Anita": 88}

  

name = input("Enter student name: ")

if name in student_marks:
    print(f"Marks of {name}: {student_marks[name]}")
else:
    print("Student not found in the record.")