# Function Practice:
# We are making a function which will return the last chracter of string.

def last_char(name):    #(name)>>>is called parameters
    return name[-1]

print(last_char("Abhishek"))  #//k  #("Abhishek")>>>>is called arguments.
print(last_char("Abhishek Mishra"))  #//a

# Now we are making a function which returns the number is even or odd.
def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
print(odd_even(10))  #//even
print(odd_even(11))  #//odd

# Now we are creating a function which will return true when the number is even else it returns false.

def is_even(num):
    if num%2 == 0:
        return True
    return False
print(is_even(10)) #//True
print(is_even(7))  #//False


# take 2 numbers as input
# create a function which tells you which one is the greatest number from above inputs.


def greater(a,b):
    if a > b:
        return a
    return b
    # else:
    #     return b

first_num = int(input("enter first number : "))
second_num = int(input("enter second number : "))
bigger = greater(first_num, second_num)
print(f"{bigger} is greater")