#take two comma seprated inputs from user
# 1. user's name
# 2. a single character

# output: 2 print lines
# 1. user's name length
# 2. count the characters that user inputed. (bonus:case sensitive counts)

name, char = input("enter comma seprated name and character: ").split(",")
print(f"length of your name is {len(name)}")

#now we use lower() method to change both name and char in same cases coz we need case sensitive counts.
#Abhishek - abhishek
#H - h
#name.lower()
#char.lower()

print(f"character count: {name.lower().count(char.lower())}")