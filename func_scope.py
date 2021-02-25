# Scope:

x = 5  # global scope/variable

def func():
    x = 7  # local scope/variable
    return x
print(func())  #//7
print(x)  #//5 