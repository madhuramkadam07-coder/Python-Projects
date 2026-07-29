#Program 1: Even or Odd Number
#Take a number from the user and print whether it is Even or Odd.

number = int(input("Enter a Number:"))
if  number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

 # Program 2: Positive, Negative, or Zero
#Take a number as input and display:
#Positive
#Negative
#Zero  

number = int(input("Enter a Number"))
if number > 0 :
    print("Number is Positive")
elif number < 0:
    print("Number is Negative")
else :
    print("Number is Zero")

#Program 3: Largest of Two Numbers
#Take two numbers and print the larger number.

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
if num1>num2 :
    print("Number 1 is larger")
elif num2>num1 :
    print("Number 2 is larger")
elif num1==num2 :
    print("Both numbers are equal")
else:
    print("Invalid Number")

#Program 4: Student Grade Calculator
#Take marks (0–100) and display:
#90–100 → Grade A
#80–89 → Grade B
#70–79 → Grade C
#60–69 → Grade D
#Below 60 → Fail

print("STUDENT DETAILS")
name = str(input("Enter the name of student:"))
div = str(input("Enter the division name:"))
rno = int(input("Enter the roll no:"))

marks = int(input("Enter the Marks"))
print("Marks of student")
if marks>=90 :
    print("Grade A")
elif marks>=80 :
    print("Grade B")
elif marks>=70 :
    print("Grade C")
elif marks>=60 :
    print("Grade D")
else :
    print("Below 60 Fail")

#Program 5: Print Numbers Using for Loop
#Print numbers from 1 to 10.

print("Displaying Numbers from 1 to 10")
for i in range (1,11):
    print(i)

#Program 6: Leap Year Checker 

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

#Program 7: Smallest of Three Numbers

a = int(input("Enter first digit"))
b = int(input("Enter second digit"))
c = int(input("Enter third digit"))

if a <= b and a <= c :
    print(a ,"is smaller")
elif b <= a and b <= c:
    print( b," is smaller")
else :
    print(c," is smaller")

#Program 8: Divisible by 5 and 11

num = int(input("Enter a number"))
if num % 5 == 0 and num % 11 == 0 :
    print("Number is divisible by ", 5 , 11)
else :
    print("Number is not divisible by ",5,11)

# Program 9: Electricity Bill Calculator

unit = int(input("Enter units consumed: "))

if unit <= 100:
    rate = 5
elif unit <= 200:
    rate = 7
else:
    rate = 10

Electricity_bill = unit * rate

print("Rate per unit =", rate)
print("Bill =", Electricity_bill)
#Program 10: BMI Calculator

weight = float(input("Enter the weight"))
height = float(input("Enter the height"))
BMI = weight / (height * height)
print("BMI =", round (BMI,2))

if BMI < 18.5 :
    print(BMI,"is underweight")
elif BMI < 25 :
    print(BMI,"is normal weight")
elif BMI < 30 :
    print(BMI,"is overweight")
else:
    print(BMI,"is Obses")


#ATM Mini System
#Requirements:
#Ask for a PIN.
#If the PIN is 1234:
#Print Login Successful
#Ask for the account balance.
#Ask for the withdrawal amount.
#If there is enough balance:
#Deduct the amount.
#Show the remaining balance.
#Otherwise:
#Print Insufficient Balance
#If the PIN is incorrect:
#Print Invalid PIN

# ATM Mini System

print("===== ATM MINI SYSTEM =====")

pin = int(input("Enter PIN: "))

if pin == 1234:
    print("Login Successful")

    account_balance = float(input("Enter Account Balance: "))
    withdraw = float(input("Enter Withdrawal Amount: "))

    if account_balance >= withdraw:
        remaining = account_balance - withdraw
        print("Withdrawal Successful")
        print("Remaining Balance:", remaining)
    else:
        print("Insufficient Balance")

else:
    print("Invalid PIN")#Program 1: Even or Odd Number
#Take a number from the user and print whether it is Even or Odd.

number = int(input("Enter a Number:"))
if  number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

 # Program 2: Positive, Negative, or Zero
#Take a number as input and display:
#Positive
#Negative
#Zero  

number = int(input("Enter a Number"))
if number > 0 :
    print("Number is Positive")
elif number < 0:
    print("Number is Negative")
else :
    print("Number is Zero")

#Program 3: Largest of Two Numbers
#Take two numbers and print the larger number.

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
if num1>num2 :
    print("Number 1 is larger")
elif num2>num1 :
    print("Number 2 is larger")
elif num1==num2 :
    print("Both numbers are equal")
else:
    print("Invalid Number")

#Program 4: Student Grade Calculator
#Take marks (0–100) and display:
#90–100 → Grade A
#80–89 → Grade B
#70–79 → Grade C
#60–69 → Grade D
#Below 60 → Fail

print("STUDENT DETAILS")
name = str(input("Enter the name of student:"))
div = str(input("Enter the division name:"))
rno = int(input("Enter the roll no:"))

marks = int(input("Enter the Marks"))
print("Marks of student")
if marks>=90 :
    print("Grade A")
elif marks>=80 :
    print("Grade B")
elif marks>=70 :
    print("Grade C")
elif marks>=60 :
    print("Grade D")
else :
    print("Below 60 Fail")

#Program 5: Print Numbers Using for Loop
#Print numbers from 1 to 10.

print("Displaying Numbers from 1 to 10")
for i in range (1,11):
    print(i)

#Program 6: Leap Year Checker 

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

#Program 7: Smallest of Three Numbers

a = int(input("Enter first digit"))
b = int(input("Enter second digit"))
c = int(input("Enter third digit"))

if a <= b and a <= c :
    print(a ,"is smaller")
elif b <= a and b <= c:
    print( b," is smaller")
else :
    print(c," is smaller")

#Program 8: Divisible by 5 and 11

num = int(input("Enter a number"))
if num % 5 == 0 and num % 11 == 0 :
    print("Number is divisible by ", 5 , 11)
else :
    print("Number is not divisible by ",5,11)

# Program 9: Electricity Bill Calculator

unit = int(input("Enter units consumed: "))

if unit <= 100:
    rate = 5
elif unit <= 200:
    rate = 7
else:
    rate = 10

Electricity_bill = unit * rate

print("Rate per unit =", rate)
print("Bill =", Electricity_bill)
#Program 10: BMI Calculator

weight = float(input("Enter the weight"))
height = float(input("Enter the height"))
BMI = weight / (height * height)
print("BMI =", round (BMI,2))

if BMI < 18.5 :
    print(BMI,"is underweight")
elif BMI < 25 :
    print(BMI,"is normal weight")
elif BMI < 30 :
    print(BMI,"is overweight")
else:
    print(BMI,"is Obses")


#ATM Mini System
#Requirements:
#Ask for a PIN.
#If the PIN is 1234:
#Print Login Successful
#Ask for the account balance.
#Ask for the withdrawal amount.
#If there is enough balance:
#Deduct the amount.
#Show the remaining balance.
#Otherwise:
#Print Insufficient Balance
#If the PIN is incorrect:
#Print Invalid PIN

# ATM Mini System

print("===== ATM MINI SYSTEM =====")

pin = int(input("Enter PIN: "))

if pin == 1234:
    print("Login Successful")

    account_balance = float(input("Enter Account Balance: "))
    withdraw = float(input("Enter Withdrawal Amount: "))

    if account_balance >= withdraw:
        remaining = account_balance - withdraw
        print("Withdrawal Successful")
        print("Remaining Balance:", remaining)
    else:
        print("Insufficient Balance")

else:
    print("Invalid PIN")
