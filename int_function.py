#int function
#We will use int function bcoz input function always takes input as string
number_one = int(input("enter first number"))
number_two = int(input("enter second number"))
sum = (number_one + number_two)
# print("total sum is " + sum) => now this too isn't work coz now the sum is in integer form and string and number cant be added so,
print("total sum is " + str(sum))