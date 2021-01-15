name= "Abhishek"
age= 24
print("hello " + name + " your age " + str(age))  #ugly syntax (python 2)
#string formatting
#python 2
#python 3
#python 3.6 (best)

print("hello {} your age is {} ".format(name, age)) #python 3

print(f"hello {name} your age is {age}")  #python 3.6

#You can do some calculations using python 3 and 3.6 like:

print("hello {} your age is {} ".format(name, age + 2))

print(f"hello {name} your age is {age + 2}")