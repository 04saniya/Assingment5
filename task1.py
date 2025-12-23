Student_marks = {  "Saniya": 85,
    "Keerti": 92,
    "Rahul": 78,
    "Anita": 88}

  

Name = input("Enter Student name: ")

if Name in Student_marks:
    print(f"Marks of {Name}: {Student_marks[Name]}")
else:

    print("Student not found in the record.")
