"""
Author: aliciarodrigo
Student ID: 122704979
Assignment 1 
Module: CS1203
"""
# Create a Python Class for a data structure OrderedList.

class OrderedList:
    pass 
# (attribute) a list of contents, that will be kept ordered at all times.
list = OrderedList()
empty = OrderedList()
str_list = OrderedList()

# (attribute) and identifier of the list, type string.
list=[1,3,5,6,4,6,4,3,5,6,3,2,8,79]
empty=[]
str_list=['hello', 'halo', 'bonjour', 'hola', 'ciao', 'olá']
class OrderedList:
    # the constructor ( init method), that takes as arguments an identifier for the list (string) and an initial content list (a list with initial contents, which may be empty or not ordered)
    def __init__(self,list):
        print(f'now running OrderedList.__init__, with {list=}') #python3.8 syntax
        self.list=list
        sorted (list)
    # a method to return the position of the first occurrence a certain element in the list
    x = list.index(6)
    print(list)
    print(sorted(list))
    print(x)
    # a method to include an element(s) in the list. The argument is a list that does not need to be ordered.
    list.append(59)
    print(sorted(list))
    # a method that searches for an element in the list, and returns the initial index and end index of that element. 
    del list[2:5]
    print(sorted(list))
    # a method to remove the first occurrence of an element in the list.
    list.remove(5)
    print(list)
    # a method that searches for an element in the list, and returns the initial index and end index of that element. 
    def find_occurrences(list, list_to_check):
        occurrences=[]
        for x, value in enumerate(list):
            if value == list_to_check:
                occurrences.append(x)
            if value == 79:
                break
        return occurrences
    print(find_occurrences(list,3))

    # an __str__ method that includes the id and current contents of the OrderedList.
    def __str__(self):
        self.list=str_list
    print (f'{list=}')
        
# Create a program that thoroughly tests all methods of your class. The program takes no input from the user (please preset variables to feed the operations). It has to initialize at least three OrderedLists, one empty, one with a pre-set Python list with ordered elements and the other with a pre-set Python list with elements out of order. One of them must be numerical, the other string.
# the constructor ( init method), that takes as arguments an identifier for the list (string) and an initial content list (a list with initial contents, which may be empty or not ordered)
    def __init__(self,str_list):
        print(f'now running OrderedList.__init__, with {str_list=}') #python3.8 syntax
        self.list=str_list
        sorted (list)
    # a method to return the position of the first occurrence a certain element in the list
    x = str_list.index('hola')
    print(str_list)
    print(x)
    # a method to include an element(s) in the list. The argument is a list that does not need to be ordered.
    str_list.append('ni hâo')
    print (str_list)
    # a method that searches for an element in the list, and returns the initial index and end index of that element. 
    del str_list[2:5]
    print(str_list)
    # a method to remove the first occurrence of an element in the list.
    str_list.remove('olá')
    print(str_list)
    # a method that searches for an element in the list, and returns the initial index and end index of that element. 
    def find_occurrences(str_list, list_to_check):
        occurrences=[]
        for y, value in enumerate(str_list):
            if value == list_to_check:
                occurrences.append(y)
            if value == 'ni hâo':
                break
        return occurrences
    print(find_occurrences(list,'bonjour'))

    # an __str__ method that includes the id and current contents of the OrderedList.
    def __str__(self):
        self.list=str_list
    print (f'{str_list=}')

    def __init__(self,empty):
        print(f'now running OrderedList.__init__, with {empty=}') #python3.8 syntax
        self.list=empty
        sorted (empty)
    # a method to return the position of the first occurrence a certain element in the list
    x = list.index(1)
    print(empty)
    print(sorted(empty))
    print(x)
    # a method to include an element(s) in the list. The argument is a list that does not need to be ordered.
    empty.append(444)
    print(sorted(empty))
    # a method that searches for an element in the list, and returns the initial index and end index of that element. 
    del empty[2:5]
    print(empty)
    # a method to remove the first occurrence of an element in the list.
    empty.remove(444)
    print(empty)
    # a method that searches for an element in the list, and returns the initial index and end index of that element. 
    def find_occurrences(empty, empty_to_check):
        occurrences=[]
        for x, value in enumerate(empty):
            if value == empty_to_check:
                occurrences.append(x)
            if value == 79:
                break
        return occurrences
    print(find_occurrences(list,23))

    # an __str__ method that includes the id and current contents of the OrderedList.
    def __str__(self):
        self.list=empty
    print (f'{empty=}')
