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
# create a function to find the greatest number from above inputs.


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


# take 3 numbers as input
# create a function to find the greatest among them.

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
num3 = int(input("enter third number : "))
largest = greatest(num1,num2,num3)
print(f"{largest} is greatest")


# Define is_palindrome function that takes one word in string as input.
# and return true if it is palindrome else return false.
#palindrome >>>> words that reads same backwards and forwards.
# example
# is_palindrome("madam") ---->>> True

# logic (algorithm)
# step 1 -> reverse the string
# step 2 -> compare reverse string with original string

def is_palindrome(word):
    reversed_word =word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

# def is_palindrome(word):
    # if word == word[::-1]:
    #     return True
    # return False

# def is_palindrome(word):
#     return word == word[::-1]

print(is_palindrome("naman"))
print(is_palindrome("horse"))