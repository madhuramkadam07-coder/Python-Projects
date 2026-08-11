#Program 1: Create and Print a Dictionary

student = {
    "name" : "Madhura",
     "age" : "19" ,
     "course" : "Bsc(ca)"
}

print("student details:",student)

#Program 2: Access Dictionary Values

student = {
    "name" : "Madhura",
     "age" : "19" ,
     "course" : "Bsc(ca)"
}

print("name:",student["name"])
print("age:",student["age"])
print("course:",student["course"])

# Program 3: Add a New Key-Value Pair

student = {
    "name": "Madhura",
    "age": 19
}

student["city"] = "Pune"

print("Updated Dictionary:", student)

# Program 4: Update a Value

student = {
    "name": "Madhura",
    "age": 19,
    "course": "BSc CA"
}

student["age"] = 20

print("Updated Student:", student)

# Program 5: Remove an Element

student = {
    "name": "Madhura",
    "age": 19,
    "course": "BSc CA"
}

student.pop("age")

print("After Removing Age:", student)

# Program 6: Print Keys and Values

student = {
    "name": "Madhura",
    "age": 19,
    "course": "BSc CA"
}

print("Keys:", student.keys())
print("Values:", student.values())

# Program 7: Print Key-Value Pairs

student = {
    "name": "Madhura",
    "age": 19,
    "course": "BSc CA"
}

print("Student Details:")

for key, value in student.items():
    print(key, ":", value)

    # Program 8: Search for a Key

student = {
    "name": "Madhura",
    "age": 19,
    "course": "BSc CA"
}

search = input("Enter a key to search: ")

if search in student:
    print("Key is found")
else:
    print("Key is not found")

# Program 9: Count Dictionary Elements

student = {
    "name": "Madhura",
    "age": 19,
    "course": "BSc CA",
    "city": "Pune"
}

print("Total elements:", len(student))

# Program 10: Student Marks Dictionary

marks = {
    "Python": 85,
    "Java": 78,
    "SQL": 90,
    "DSA": 82
}

print("Student Marks:", marks)
print("Python Marks:", marks["Python"])
print("Highest Marks:", max(marks.values()))
print("Lowest Marks:", min(marks.values()))

# Day 7 Challenge: Student Management System

student = {
    "name": "Madhura",
    "age": 19,
    "course": "BSc CA",
    "city": "Pune"
}

# Take marks from user
python_marks = int(input("Enter Python marks: "))
java_marks = int(input("Enter Java marks: "))
sql_marks = int(input("Enter SQL marks: "))

# Add marks to dictionary
student["Python"] = python_marks
student["Java"] = java_marks
student["SQL"] = sql_marks

# Calculate results
total = python_marks + java_marks + sql_marks
average = total / 3
highest = max(python_marks, java_marks, sql_marks)

# Display report
print("\n===== STUDENT REPORT =====")

for key, value in student.items():
    print(key, ":", value)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")