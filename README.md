task 1 :
Student_marks = {  
    "Saniya": 85,
    "Keerti": 92,
    "Rahul": 78,
    "Anita": 88
}
This is a dictonary !
Student name = key
Student marks = value

Name = input("Enter Student name: ")
Asks the user to type a student’s name
Stores whatever the user types in the variable Name

if Name in Student_marks:
it checks if" Does this student exist in our marks register?”

print(f"Marks of {Name}: {Student_marks[Name]}")
Fetches the marks of that student
Prints them

task2:
Numbers = list(range(1, 11))    #generates numbers from 1 to 10 and converts the range into a list.
first_five = Numbers[:5]       #extracts the first five elements from the list.## list [start : end] logic.
reversed_list = first_five[::-1]     # [::-1] reverses the extracted list. ##list [start : end : step]
print("original List:", Numbers )
print("Extracted List:", first_five)
print("Reversed List:", reversed_list).

