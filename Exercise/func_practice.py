# Function Practice:
# We are making a function which will return the last chracter of string.

def last_char(name):    #(name)>>>is called parameters
    return name[-1]

print(last_char("Abhishek"))  #//k  #("Abhishek")>>>>is called arguments
print(last_char("Abhishek Mishra"))  #//a

# Now we are making a function which returns the number is even or odd.
def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
print(odd_even(10))  #//even
print(odd_even(11))  #//odd

# Now we are making a function which will return true when the number is even else it returns false.

def is_even(num):
    if num%2 == 0:
        return True
    return False
print(is_even(10)) #//True
print(is_even(7))  #//False
