# Problem No:1
# sum of n natural numbers
# ask user for naturak number(n)
# print total from 1 to n

number = input("please enter a number")
number = int(number)
total = 0
i = 1
while i <= number:
    total += i
    i +=1
print(total)


# Problem No:2
# ask user to input a number more than one digit
# example- 1256
# calculate 1+2+5+6 and print


# algorithm - (method to solve problem in human language)
# ask input in string, i.e. don't change string to int
# example - "1256"
# pick string integer one by one and vhange into integer
# int(example[0]) + int(example[1]) + ... go to len(example)
 
number = input("enter a number of more than 1 digit: ")
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)
