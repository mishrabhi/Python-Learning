# EXERCISE - WATCH COCO
# Ask user's name and age
# If user's name start with 'a' or 'A' and age is above or equal to 10 then
# Print 'You can watch coco movie'
# Else print 'sorry, you cannot watch coco'

user_name = input("enter your name")
user_age = input("enter your age")
user_age = int(user_age)
if user_age >= 10 and (user_name[0] == 'a' or user_name[0]== 'A'):
    print('You can watch coco movie')
else:
    print('Sorry, you cannot watch movie')
