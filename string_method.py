#String Methods:

name = "AbhISHeK MIsHra"

# 1.len() function => It counts the character in string.It includes spaces too.
print(len("Abhishek"))  #//8
print(len(name))  #//15  (with space)
print(len("AbhishekMishra")) #//14  (Without space)

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


#6.strip() method => It removes spaces from left or right in the string.
# lstrip() => to remove spaces from left side.
# rstrip() => to remove spaces from right side.
place = "     Prayagraj      "
dots = "................"
print(place + dots)  #//       Prayagraj     .............
print(place.lstrip() + dots) #//Prayagraj     ............
print(place.rstrip() + dots) #//         Prayagraj...........
print(place.strip() + dots) #//Prayagraj........... 



# 7. replace() method: It is used for replacements.
#syntax => string.replace("old content" , "new content"
string = "Capital of India is Delhi."
print(string.replace(" " , "_"))  #//Capital_of_India_is_Delhi.