# Program 1: Print a String

name = input("Enter your name: ")

print("Name:", name)
print("Number of characters:", len(name))

#Program 2: Length of a String

string = input("Enter a string:")

print("String:",string)
print("Length of string:",len(string))

# Program 3: Convert to Uppercase

text = input("Enter a string: ")

print("Original String:", text)
print("Uppercase String:", text.upper())

# Program 4: Convert to Lowercase

text = input("Enter a string: ")

print("Original String:", text)
print("Lowercase String:", text.lower())

# Program 5: Count Vowels

sentence = input("Enter a string: ")

count = 0

for ch in sentence:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
       ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        count += 1

print("Total vowels =", count)

#Program 6: Reverse a String

text = input("Enter a String")
print("Original string:",text)
print("Reverse string:",text[::-1])

#Program 7: Palindrome Checker

string = input("Enter a string")

reverse = string[::-1]
if text==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# Program 8: Count Words

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Total words =", len(words))


# Program 9: Find a Character

text = input("Enter a string: ")
ch = input("Enter a character to find: ")

position = text.find(ch)

if position != -1:
    print("Character found at index", position)
else:
    print("Character not found")

    # Program 10: Replace a Word

sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

result = sentence.replace(old_word, new_word)

print("Updated sentence:")
print(result)


# Password Strength Checker

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("✅ Strong Password")
else:
    print("❌ Weak Password")