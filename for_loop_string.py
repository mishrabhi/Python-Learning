# for_loop_string:

# Method used in all programming languages:
name = "Abhishek"
for i in range(len(name)):
    print(name[i])  

# Method used in python for the same:
name = "Abhishek"
for i in name:     # you can write this too: for i in "Abhishek":
    print(i) 


# 1256 ---> 1+2+5+6
num = input("enter a number : ")
total = 0
for i in num:
    total += int(i)
print(total)  #// 9