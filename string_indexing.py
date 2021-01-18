#string indexing
language = "python"

# positions(index number)

# p = 0  
# y = 1
# t = 2
# h = 3
# o = 4
# n = 5

print(language[2]) #//t #we use square brackets to print using indexing.
print(language[4]) #//o

#If we try to do indexing backwards,then:

# p = -6
# y = -5
# t = -4
# h = -3
# o = -2
# n = -1

print(language[-5]) #//y
print(language[-3])  #//h




#=> String_slicing:-
#when we want to print more than one characters using indexing,then we use string slicing:
lang = "Python"
#print(lang[4])  //o
#syntax - [start argument : stop argument - 1 ]

#output: py
print(lang[0:2])  #//Py
#output: ytho
print(lang[1:5])  #//ytho   

print(lang[:]) #//Python (=>If we dont give arguments,it prints everything.)
print(lang[1:]) #//ython (=>If we only give start argument,it print from start argument to end.)
print(lang[:4]) #//Pyth  (=>If we only give stop argument,it prints all before that.)

#We can either use above as this too:
print("Abhishek"[1:5]) #//bhis 


#=>String Argument Slicing:-
#it is same like string slicing but we can give step to the start and stop arguments.
#syntax: [start argument : stop argument-1 : step]
print("Harshit"[0:5:1])  #// Harsh
print("Harshit"[0:5:2])  #// Hrh 
print("Abhishek"[0:7:3])  #//Aie
print("Abhishek"[5::-1])  #//hsihbA