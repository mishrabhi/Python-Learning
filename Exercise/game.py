# MODIFY NUMBER GUESSING GAME:

# you have to guess a number between 1 to 100 
# If you have guessed lower than the winning number then it prints too low
# If you have guessed higher than the winning number then it prints too high.
# It give you unlimited attempts to guess the winning number.
# It also prints in how many times you have guessed the winning number correctly.
# It also selects random numbers when you had guessed winning num and trying next time. 

import random
winning_num = random randint(1,100)
guess = 1
number = int(input("guess a number between 1 and 100 : "))
game_over = False

while not game_over:
    if number == winning_num:
        print(f"you win, and you have guessed this number in {guess} times")
        game_over = True
    else:
        if number < winning_num:
            print("too low")
            guess += 1
            number = int(input("guess again : "))
        else:
            print("too high")
            guess += 1
            number = int(input("guess again : "))  




# DRY (Don't Repeat Yourself) Method:

import random
winning_num = random.randint(1,100)
guess = 1
number = int(input("guess a number between 1 and 100 : "))
game_over = False

while not game_over:
    if number == winning_num:
        print(f"you win, and you have guessed this number in {guess} times")
        game_over = True
    else:
        if number < winning_num:
            print("too low")
            
        else:
            print("too high")

        guess += 1          #You can use thee 2 lines only once.
        number = int(input("guess again : "))    
    