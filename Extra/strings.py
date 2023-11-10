# String manipulation is a common topic in programming interviews, and Python provides powerful built-in functions and methods for working with strings. Here are some important string manipulation questions and tips in Python to help you prepare for interviews:
name = "Landon"


# 1. Reverse a String:
#   Using slicing: string[::-1]
#   Using the reversed() function: "".join(reversed(string))
reversedName1 = name[::-1]
reversedName2 = "".join(reversed(name))
print(1, reversedName1, 2, reversedName2)


# 2. Check if a String is Palindrome:
#   Using slicing: string == string[::-1]
palindrome = "racecar"
if(palindrome == palindrome[::-1]):
    print(palindrome + " is a palindrome!")
else:
    print(palindrome + " is not a palindrome!")

# 3. Count the Occurrence of a Character in a String:
#   Using the count() method: string.count(character)
wordWithLetters = "Mississippi"
letterCount = wordWithLetters.count("s")
print(wordWithLetters, letterCount)

# 4. Remove Duplicates from a String:
#   Using a set: "".join(set(string))
#   Using a dictionary: "".join(dict.fromkeys(string))


# 5. Check if Two Strings are Anagrams:
#   Using sorted strings: sorted(string1) == sorted(string2)
#   Using dictionaries:
#   python
#   from collections import Counter
#   Counter(string1) == Counter(string2)


# 6. Split a String into Words:

# Using the split() method: string.split()


# 7. Join a List of Strings into a Single String:

# Using the join() method: " ".join(list_of_strings)


# 8. Find the Longest Common Prefix among Strings:

# Using the zip() function and a loop:
# python
# Copy code
# for i, letters in enumerate(zip(*strings)):
#     if len(set(letters)) > 1:
#         common_prefix = strings[0][:i]
#         break
# else:
#     common_prefix = min(strings)



# 9. Convert String to Integer:

# Using the int() function: integer = int(string)


# 10. Convert Integer to String:

# Using the str() function: string = str(integer)
# Tips:

# Familiarize yourself with the built-in string methods in Python, such as split(), strip(), join(), replace(), startswith(), endswith(), etc.
# Understand how string slicing works and its various use cases.
# Take advantage of Python's in operator to check if a substring exists in a string.
# Make use of the len() function to get the length of a string or a list.
# Consider using regular expressions (re module) for more complex string manipulation tasks.
# Practice coding these string manipulation questions and ensure you understand the time and space complexities of your solutions.
# Remember to analyze and optimize your code, handle edge cases, and write clean and readable code during interviews. Good luck!