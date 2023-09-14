"""
Author: aliciarodrigo
Student ID: 122704979
Assignment 3
"""

# PART 1
# Code for new user in sytem created through function.
# Code = surname, year of birth, first two letters of first name, two random digits between 0 & 9. Function takes two strings (name and surname) and integer (year), & reurns code. 
# Define function.

def username(letter0, letter1, surname, year):
    str1 = surname + year + letter0 + letter1
    return (str1)

# Create loop 
for i in range (3):
    # import random function
    import random

    # User input 
    l = input ('name : ')
    s = input('surname: ')
    y = input('date of birth: ')

    # Random function as variable definition.
    random_1 = random.randint (0,9)
    random_2 = random.randint (0,9)

    # Import function and print
    user = username (l[0], l[1],s,y)
    print(user,random_1,random_2)

# PART 2
# Create a function in Python that takes as parameter a string and returns the number of characters in that string that are digits (that is ’0’ , ’1’, ’2’, etc.).
# Test your function by creating a code that reads from the user 4 strings (by means of a for loop and, for each of those strings, calls the function developed in question 3, then prints the result.
# Create lopp 4 times.
for i in range (4):
# def function
    def count_numbers(str):
    # set count to 0
        count = 0
        for i in str:
        # every digit it adds 1
            if i.isdigit():
                count+-1
        return (count)

# Input sentence
s = input("Enter sentence: ")
# Create var & call function.
final_count = count_numbers(s)
# Print result
print("Amount of numbers in sentence is: ", final_count)

