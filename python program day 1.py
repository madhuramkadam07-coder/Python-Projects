# Program 1: Personal Information #Store and print: #Store and print:
#Name
#Age
#College
#Branch
name = "Madhura"
age =  19
stream = "Bsc(computer application)"
college = "Dr D.Y.Patil ACS College Pimpri , Pune 18"

print("Name:",name)
print("Age: ", age)
print("Stream",stream)
print("College",college)

# Program on data types

name = "Madhura"
age = 19
fy_result= 9.64
student = True

print(type(name))
print(type(age))
print(type(fy_result))
print(type(student))

#Program on User Input 

name = input("Enter your name:")
age = input("Enter your Age:")
city = input("Enter you city:")

print("Details of Person")
print("Name of person",name)
print("Age of person",age)
print("City of person",city)

#Program 4: Arithmetic Calculator
#Take two numbers and perform:
#Addition
#Subtraction
#Multiplication
#Division
#Modulus

a = int(input("Enter first number"))
b = int(input("Enter second number"))

print("Arithmetic Operations of number:")
print("Adittion :", a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modules:",a%b)

#Program 5: Rectangle Area & Perimeter
#Take:
#Length
#Width

#Calculate:
#Area
#Perimeter

length = float(input("Enter length of rectangle"))
width = float(input("Enter width of rectangle"))

print("Details of rectangle")
print("Area of rectangle:" , length*width)
print("Perimeter of rectagle:",2*(length+width))

#Program 6: Swap Two Numbers (Without Third Variable)
#Take two numbers and swap their values.

a = int(input("Enter first number"))
b = int(input("Enter second number"))
a = a + b
b = a - b
a = a - b
print("After swapping")
print("a=",a)
print("b=",b)

#Program 7: Celsius to Fahrenheit
#Formula:
#F = (C × 9/5) + 32

celsius = float(input("Enter the celsius unit"))
fahrenhite = (celsius * 9 / 5) +32
print("Temperature of Fahrenheit is ",fahrenhite)

#Program 8: Simple Interest Calculator
#Formula:
#SI = (P × R × T) / 100

principal = float(input("Value of principal:"))
rate = float(input("Value of rate "))
time = float(input("Value of time "))

SI = (principal * rate * time) / 100
print("Value of SI is",SI)

#Program 9: Circle Area & Circumference

radius = int(input("Enter radius of radius"))
PI = 3.14
area = PI * radius * radius
circumference = 2 * PI * radius

print("Area and Circumference of circle is", area,circumference)

#Program 10: Currency Converter
#Convert Indian Rupees to US Dollars.

rupees = float(input("Enter the amount in rupees"))
usd = rupees / 83
print("Amount in dollar ($)",round(usd,2))

#Student Information System
print("========Student information system=====")
name = str(input("Enter the name of student:"))
age = int(input("Enter Age of student:"))
college = str(input("Enter the College:"))
branch = str(input("Enter the branch name:"))
rollno = int(input("Enter the Roll no:"))

subject1 = float(input("Enter subject1 marks:"))
subject2 = float(input("Enter subject2 marks:"))
subject3 = float(input("Enter subject3 marks:"))

total = subject1 + subject2 + subject3
average = total/ 3

print("Student details")
print("Name:",name)
print("Age:",age)
print("College:",college)
print("Branch:",branch)
print("Roll no",rollno)

print("Student Marks")
print("Subject1 marks:",subject1)
print("Subject2 marks:",subject2)
print("Subject3 marks:",subject3)
print("Total of marks:",total)
print("Average of marks:",average)