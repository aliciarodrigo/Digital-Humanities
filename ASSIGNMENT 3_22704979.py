"""
Author: aliciarodrigo
Student ID: 122704979
Assignment 3
Module: CS1203
"""
# create a class
import random
from urllib import request
import nltk, re, pprint
nltk.download('punkt')
from nltk import word_tokenize
from priority_queue import prior_queue
# Create a class GBook
class GBook:
    # an attribute named link, which contains a string defining a link to the book on Gutenberg project.
    att_link = "http://www.gutenberg.org/cache/epub/11917/pg11917.txt"
    # an attribute Title.
    att_title = 'book title:'
    # anattributeAuthor
    att_author = 'book author:'
    # an attribute representing an identifier, generated randomly between 1010 and 999999.
    def identify():
        att_id = random
        for i in range(1010-999999):
            if len(random)>0:
                return (random)
    att_title = 'book title:'
    att_author = 'book author:'
    # The constructor, which has as argument the link to the book in the Gutenberg project.
    def __init__(self, att_link):
        att_link = "http://www.gutenberg.org/cache/epub/11917/pg11917.txt"
    # A method to load the text version of the book from its page in the project and return the corresponding string with the book contents.
    def load_text():
        att_link = "http://www.gutenberg.org/cache/epub/11917/pg11917.txt"
        response = request.urlopen(att_link)
        raw = response.read().decode()
        return
    # A method to set title of book by extracting it from corresponding string book contents.
    def title_extract():
        att_title = "book title:"
        att_link = "http://www.gutenberg.org/cache/epub/11917/pg11917.txt"
        response = request.urlopen(att_link)
        raw = response.read(att_title).decode()
        return(att_title)
    # A method to set the author of the book by extracting it from the book’s string content.
    def author_extract():
        att_author = "book author:"
        att_link = "http://www.gutenberg.org/cache/epub/11917/pg11917.txt"
        response = request.urlopen(att_link)
        raw = response.read(att_author).decode()
        return(att_author)
    # A method to extract the tokens of the book, and return their list.
    def tokenize():
        listing = []
        att_tokens = "tokens: "
        att_link = "http://www.gutenberg.org/cache/epub/11917/pg11917.txt"
        response = request.urlopen(att_link)
        raw = response.read(att_tokens).decode()
        listing.append (att_tokens)
        # A print method to print the book’s title, author and size (number of characters).
        print(listing)
    print (att_title, att_author, 'number of characters: ', len(tokenize))
    # Create two books.
    class book_1:
        book_url = "https://www.gutenberg.org/cache/epub/70563/pg70563-images.html"
    class book_2:
        book_url_2 = "https://www.gutenberg.org/cache/epub/70560/pg70560-images.html"
# Load at least one of them and test all methods for it.
c1 = GBook 
c1.book_1()
# From the list of tokens, create a priority queue with the words that start with the first letter of your first name. The word has priority 1 if it has less than 4 letters, 2 if has between 4 and 6 letters, and priority 3 if it has more than 6 letters.
def priority_queue():
    att_priority = prior_queue()
    a_words = ['altar','alliviate', 'allow', 'alianate', 'arcane', 'able', 'awesome', 'aquire', 'amazing', 'aquatic', 'aspire', 'affect', 'apex', 'ape', 'appreciate', 'apathy', 'amicable', 'abandon', 'absence', 'acceptable']
    prior = {{'priority_1': ('value1'<4), 'priority_2':('value2',4-6),'priority_3':('value3'>6)}}
# As you remove all items from the queue one by one, print all those with top priority, and 20 of each with other priorities.
    a_words = prior_queue()
    for i in range (20):
        a_words.get()
        break
    print (prior = {{'priority_1': ('value1'<4)}})
# Messages are printed all throughout the code in order for it to be traceable for those who may run the program. 