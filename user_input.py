#user input
#input function
name = input("enter your name ")
print("hello " + name)
age = input("enter your age ")
print("hello " + name + " " + "your age is " + age)
marriage = input("are you marrried? ")
print("hello " + name + " " + "your age is " + age + " " + "and you are " + marriage + " " + "married")


#=>You can give two inputs in a single line:
# name= input("enter your name")
# age= input("enter your age")
name, age = input("enter your name and age ").split()
#you have to give space between name and age like:
#enter your name and age Abhishek 23
print(name)
print(age)