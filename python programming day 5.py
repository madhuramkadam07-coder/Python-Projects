#Program 1: Create and Print a List

fruits = ["Apple","Guava","Chikoo","Pomogranet","Grapes"]
print("Fruits list:")
print(fruits)

#Program 2: Access List Elements

colors = ["White","Purple","Blue","Black","Orange"]
print("List of colors according to position")

print("First element",colors[0])
print("Third element",colors[2])
print("Last element",colors[-1])

# Program 3: Add Elements

numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(1, 15)

print("Updated List:", numbers)

# Program 4: Remove Elements

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.remove("Banana")
fruits.pop()

print("Updated List:", fruits)

# Program 5: Length of List

numbers = [10, 20, 30, 40, 50]

print("Length of List:", len(numbers))

# Program 6: Sum of List Elements

numbers = [10, 20, 30, 40, 50]

total = sum(numbers)

print("Sum =", total)

# Program 7: Largest and Smallest Number

numbers = [12, 45, 7, 89, 34]

print("Largest Number:", max(numbers))
print("Smallest Number:", min(numbers))

# Program 8: Sort a List

numbers = [45, 12, 89, 7, 34]

print("Original List:", numbers)

numbers.sort()
print("Ascending Order:", numbers)

numbers.sort(reverse=True)
print("Descending Order:", numbers)


# Program 9: Search an Element

names = ["Madhura", "Rahul", "Sneha", "Amit", "Priya"]

search = input("Enter a name to search: ")

if search in names:
    print(search, "Found in the list")
else:
    print(search, "Not Found")


    # Program 10: Reverse a List

numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print("Reversed List:", numbers)


# Student Marks Analyzer

marks = []

for i in range(1, 6):
    mark = float(input("Enter marks of Subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\n===== RESULT =====")
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")