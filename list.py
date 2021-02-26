# data structure
# ordered collection of items
# you can store anything in lists like int, float, string
# [] ---->>> syntax of list

num = [1, 2, 3, 4]
print(num)

words = ["Abhishek", "Word2", "Word3", "Word4"]
print(words)
print(words[:2])  #// ['Abhishek', 'Word2']   -->> you can use slicing to print two or more than two contents.

mixed = [1, 2, 3, 'Four', 'Five', 2.4, None, True]
print(mixed)
print(mixed[4])   #you can use indexing to print particular string or num
mixed[2] = 'Two'  
print(mixed)    #// [1, 2, 'Two', 'Four', 'Five', 2.4, None, True]  -->>you can change any content using indexing.


# how to add items in our list
# most common thing that you can do with your list and most important.
# We use append --->>> it adds items at last of your list.
fruits = ['grapes', 'apple']
fruits.append('mango')
print(fruits)    #// ['grapes', 'apple', 'mango']

