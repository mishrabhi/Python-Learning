# FUNCTION:
# name = "Abhishek"
# print(len(name))  #//8 (Here (len) is the prebuild function.)

def add_two(num1,num2):
    return num1+num2

# # total = add_two(2,4)
# # print(total)    #//6
# print(add_two(2,4))  #//6

a = int(input("enter first number : "))
b = int(input("enter second number : "))
total = add_two(a,b)
print(total)


first_name = input("enter first name ")
last_name = input("enter last name ")
print(add_two(first_name,last_name))
