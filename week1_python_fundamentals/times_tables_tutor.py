# Additions
# Invite user to enter their name
# Write scores to a file
# Expand this file to include high score
from random import randint

points_counter = 0

question_counter = 0

while question_counter < 10:
    
    question_counter += 1

    num1 = randint(2, 12)
    
    num2 = randint(2, 12)

    init_input = int(input(f"what is {num1} x {num2}: "))

    wrong_counter = 1

    while wrong_counter < 3:

        if init_input != (num1 * num2):

            print("Incorrect - try again.")

            init_input = int(input(f"what is {num1} x {num2}: "))

            wrong_counter += 1

        else:

            print("Correct!")
            
            points_counter += 1

            break

        if wrong_counter == 3:

            print("Let's move on to another question.")

again = input(f"You got {points_counter}. Press (y) to try again or (q) to quit ")

if again == 'y':

    question_counter = 0
    
else:

    pass




