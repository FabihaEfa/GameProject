###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#

#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!


import random
digits = list(range(10))
random.shuffle(digits)
computer_guess = digits[:3]

cg_string=''
for char in computer_guess:
    cg_string += str(char)

print("\n\n\n******* Welcome to CODE BREAKER GAME !! ******* \n\n1. The computer will think of 3 digit number that has no repeating digits.")
print("2. You will then guess a 3 digit number ")

#print(cg_string)


for i in range(1000):
    guess = input("\n\nWhat is your 3 digit guess?\n")
    #print(guess)
    if len(guess) != 3:
        print("please write 3 digit number")
    elif guess.isdigit() == False:
        print("Please give a number")
    else:
        if guess[0]==cg_string[0] and guess[1]==cg_string[1] and guess[2]==cg_string[2]:
            print("Perfect Match: You've guessed perfect match for all digits")
            exit()


        elif guess[0]==cg_string[0] or guess[1]==cg_string[1] or guess[2]==cg_string[2]:
            print("Match: You've guessed a correct number in the correct position")

        elif guess[0]==cg_string[1] or guess[1]==cg_string[2] or guess[2]==cg_string[0] or guess[0]==cg_string[2] or guess[1]==cg_string[0] or guess[1]==cg_string[1] or guess[2]==cg_string[1]:
            print("Close: You've guessed a correct number but in the wrong position")

        else:
            print("Nope: You haven't guess any of the numbers correctly")





# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
