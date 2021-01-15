#python is a dynamic programming language.
#we can store numbers as well as string in variables

number1 = 123
print(number1)
number1 = 321
print(number1)

name = "Raja"
print(name)
name = "Satyam"
print(name)

#You cannot start variable names using numbers or any special characters except underscore(_).Example: 1user
#You can start variable names using letters and _  Example: number1, _number

#you can mostly use snake case writing when writing python 
user_one_name = "Ashutosh"
print(user_one_name)

#you can use camel casing also.But people mostly use camel using in writing java.
userOneName = "Abhishek"
print(userOneName) 



#=> You can assign multiple variables in a single line 
name, age = "Abhishek", "24"
print("hello my name is " + name + " and my age is " + age)

x=y=z=1
print(x+y+z)