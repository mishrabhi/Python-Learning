# EXERCISE , NUMBER GUESSING GAME
# Make a variable, winning_number and assign number to it.
# Ask user to guess a number.
# if user guessed correctly then print "You Win !!"
# if user didn't guessed correctly then :
    #if user guessed lower than actual number then print "too low!"
    #if user guessed higher than actual number then print "too high!"

winning_num = "65"
guessing_num = (input("guess a number between 50 to 100 "))
if winning_num == guessing_num:
    print("You win!!")
else:   #nested if else statement
    if guessing_num < winning_num:
        print("too low!")
    else:
        print("too high!")