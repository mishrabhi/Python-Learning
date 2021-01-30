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
