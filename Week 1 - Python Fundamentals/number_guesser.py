import math

print("Pick a number between 1 and 100 (inclusive)\n")

lower = 1

upper = 100

guess = (lower + upper) // 2

print(f"My guess is: {guess}")

while True:
    
    feedback = input("Is my guess too low (l), too high (h), or correct (c)? ")

    if feedback == 'l':

        lower = guess + 1

        guess = math.ceil((lower + upper) / 2)

    elif feedback == 'h':

        upper = guess - 1

        guess = math.floor((lower + upper) / 2)

    elif feedback == 'c':

        print("I got it!")

        break

    else:

        print("Invalid input, please enter 'l', 'h', or 'c'.")

    print(f"My guess is: {guess}")