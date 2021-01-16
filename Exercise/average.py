#Ques: Ask user to put 3 numbers and you have to print average of three numbers using string formatting.

#Bonus: try to take all three comma seprate inputs in one line.

num1, num2, num3 = input("enter three numbers comma seprated ").split(",")
print(f"aveage of three numbers is {(int(num1) + int(num2) + int(num3)) / 3}") 