#Program 1: Print 1 to 10 using while
#Concept: while loop

print("Numbers from 1 to 10 :")
i = 1

while i <= 10:
  print(i)
  i = i + 1

#Program 2: Multiplication Table
#Take a number from the user and print its multiplication table (1–10).

print("Multiplication table from 1 to 10 :")
for i in range(1,11):
  print("Table of ",i)

  for j in range(1,11):
    print(i,"x",j,"=", i*j)

#Program 3: Sum of First N Numbers
#Take a number N.

num=int(input("Enter the no of elements"))

sum = 0
i = 1
while i<=num:
 total = sum + i
 i = i+1
print("Sum of first ",num ,"numbers is", total) 

# Program 4: Factorial of a Number

num = int(input("Enter a number: "))

i = 1
fact = 1

while i <= num:
    fact = fact * i
    i += 1

print("Factorial of", num, "is", fact)

#Program 5: Reverse Counting
#Print numbers from 10 to 1 using a while loop.

print("Numbers from 10 to 1:")
i = 10
while i >= 1:
  print(i)
  i = i - 1

  # Program 6: Print Even Numbers (1-100)

print("Even Numbers from 1 to 100")

i = 1

while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

    # Program 7: Print Odd Numbers (1-100)

print("Odd Numbers from 1 to 100")

i = 1

while i <= 100:
    if i % 2 != 0:
        print(i)
    i += 1

    # Program 8: Prime Number Checker

num = int(input("Enter a number: "))

count = 0
i = 1

while i <= num:
    if num % i == 0:
        count += 1
    i += 1

if count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")

    # Program 9: Count Digits

num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits =", count)

# Program 10: Reverse a Number

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num = num // 10

print("Reverse number =", reverse)

  #Number Guessing Game
#Requirements
#Store a secret number (for example 7).
#Ask the user to guess the number.
#If the guess is correct:
#Print "Congratulations! You guessed it."
#Otherwise:
#Print "Wrong guess. Try again."
#Keep asking until the correct number is entered (use a while loop).

# Number Guessing Game

print("=========== Guess the Number Challenge =============")

secret_number = 7

guess = int(input("Guess the number: "))

while guess != secret_number:
    print("Wrong Guess... Try Again.")
    guess = int(input("Enter your guess again: "))

print("🎉 Congratulations! You guessed it.")
