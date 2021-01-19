#String Methods:

name = "AbhISHeK MIsHra"

# 1.len() function => It counts the character in string.It includes spaces too.
print(len("Abhishek"))  #//8
print(len(name))  #//15
print(len("AbhishekMishra")) #//14

# 2.lower() method => It converts all characters into lower cases.
print(name.lower())  #// abhishek mishra
lower = name.lower()
print(lower)  #// abhishek mishra

# 3.upper() method => It converts all characters into upper cases.
print(name.upper())  #// ABHISHEK MISHRA 

# 4.title() method => It converts only first letter of string in upper case.
print(name.title())  #//Abhishek Mishra

# 5.count() method => It counts a particular character in a string.
print(name.count("H"))  #//2