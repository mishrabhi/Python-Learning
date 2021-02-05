# sum from 1 to 10
# 1+2+3+.....10

total = 0
for i in range(1,11):
    total += i
print(total)  #//55

# Ask user a number and then print the sum from 1 to that number:

number = int(input("enter a number: "))
total = 0
for i in range(1,number+1):
    total += i
print(total)