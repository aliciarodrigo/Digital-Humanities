"""
Created on Mon Jan 16 20:37:13 2023
@author: alicia rodrigo
"""
# empty list
l1 = []

# insert 2 strings into list above
str1 = 'hello'
str2 = 'hello back'

l1.append (str1)
l1.append (str2)

# print the list
print (l1)

# exchange the content of two variables. Attribute the values to the variables first
str1 = input ('enter value for str1 = ')
str2 = input ('enter value for str2 = ')
temp = str1
str1 = str2
str2 = temp
print(str1, str2)
# remove an element from a list by its content
l1.remove ('goodbye back')

# remove an element from the last position of the list
l1.pop(str2)

# find the index of an element in the list
index = l1.index ('str1')
print(index)

# create a function to count how many times a particular element appears in a list. I will start it for you:
count = l1.count ()

# test the function above, by creating a list with names of cities, and then looking for 'Cork' 
l2 = ['Cork', 'Madrid', 'Barcelona', 'Galway', 'Belfast']
count = l2.count ('Cork')

# what happens if 'Cork'  is not in the list = an error occurs?

# create a function yourself to reverse a list, that is, if the list is ['a','b','c'] then the reverse is ['b','c','a']
l3 = ['a','b','c']
l3.reverse()
print (l3)
