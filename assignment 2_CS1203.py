"""
Author: aliciarodrigo
Student ID: 122704979
Assignment 2
Module: CS1203
"""
import random 
from simplequeue_2023 import simple_queue
from simplestack_2023 import simple_stack
# Write a program to trace a route for a road trip.
# Names of at least 20 localities in Ireland in a separate text file. 
# Function to read from a file with names and return list with names. Function receives as argument the name of file. 
def localities (file):
    file = open (file,'r')
    lists = [line.strip() for line in file.readlines()]
    file.close()
    return lists
# Function to draw N names from list of names randomly. It receives as arguments the original list and N, and returns another list with N names drawn. 
def random_names(name_rand, quantity_of_names):
    names = []
    for i in range (quantity_of_names):
        name = random.randint(0, len(name_rand))
        names.append (name_rand[name])
    print (names)
# Draw 5 localities randomly from first function with function 2.
list1 = localities ('localities.txt')
names = random_names (list1, 10)
print(names)
# add localities from list to queue.
queue_locals = simple_queue()
queue_locals.put(names)
# Trace way out by removing localities one by one from queue, printing locality name. adding the locality to a stack.
stack_locals = simple_stack()
for i in range (19):
    queue_locals.get()
    stack_locals.push(queue_locals)
    break
# trace way back on your road trip, writing code to remove the localities from the stack one by ome amd print their names until stack is empty and you're back home. 
for i in range (19):
    stack_locals.pop()
    break