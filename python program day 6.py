#Program 1: Create and Print a Tuple

fruits = ("apple","banana","Guava","Orange","Kiwi")

print("Fruit Tuples:",fruits)

#Program 2: Access Tuple Elements

flowers = ("Rose","Lily","Jasmine","Sunflower","Marigold")

print("First element:",flowers[0])
print("favourite flower:",flowers[1])
print("Last element:",flowers[-1])

#Program 3: Count an Element in Tuple

numbers = (10,20,30,40,50,60)

print("60 is present :",numbers.count(60),"times")

# Program 4: Find Index in Tuple

animals = ("dogs", "cats", "zebra", "tiger")

print("Zebra is present at:", animals.index("zebra"), "Position")

#Program 5: Tuple Unpacking

person_details = ("Madhura",19,"IT field")

name,age,Career  = person_details
print("Name of person:",name)
print("Age of person:",age)
print("Course :",Career)

#Program 6: Create and Print a Set

numbers = {1,2,3,4,5,6,7,8,9,10}

print("Numbers:",numbers)

# Program 7: Add and Remove Elements in a Set

numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

numbers.add(110)
numbers.remove(80)

print("Updated Set:", numbers)

#Program 8: Union of Two Sets

set1 = {1,2,3,4}
set2 = {5,6,7,8}

print("Union of sets:",set1.union(set2))

#program 9: Intersection of Two sets

set1 = {1,3,5,7}
set2 = {2,4,6,8}

print("Intersection of sets are:",set1.intersection(set2))

#Program 10: Search in Set

numbers = {10,20,30,40,50}

num = int(input("Enter a number:"))

if num in numbers :
    print("Number is found")
else:
    print("Number not found")


#Day 6 Challenge: Student Data Using Tuple & Set

student = ("Madhura", 19, "BSc CA")

subjects = {"Python", "Java", "C", "HTML", "Python"}

print("Student:", student)
print("Subjects:", subjects)
print("Unique Subjects:", len(subjects))

if "Python" in subjects:
    print("Python is available")
else:
    print("Python is not available")