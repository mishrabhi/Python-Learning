#Since we cannot use "double quotes" inside "double quotes" so now we can use it by applying backslash.
print("hello \"world\" World")
print('I\'m Iron Man')

#We can use \n to form a new line.
print("line A\nline B")
print('line A\nline B\nline C')

#We can use \t for tab(creates a tab space)
print("name\tharshit")

#If you want to print backslash(\) then you have to use double blackslash(\\).
print("This is backslash \\")
print("This is double blackslash \\\\")

#Escape Sequence as a Normal Text:
#output:line A \n Line B
print("Line A \\n Line B")

#output:line A \t line B
print("line A \\t line B")

#output:this is 4 backslash \\\\
print('this is 4 backslash \\\\\\\\')

#output: \" \'
print(" \\\" \\\' ")

#Raw String:
#this is a shortcut for using escape characters as normal text
print(r"line A \n line B")
#it always prints the same as normal text if we put r first.