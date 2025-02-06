
"""
Write a Python scripts that implements the “Guess the Number” game.

The script will generate of a random integral number (use the module random) from 1 to 100, and ask you to guess it.

The script will tell you if each guess is too high or too low.

You win if you can guess the number within six tries.

Note: to generate the random secret number you can use:
    
    random.randint(a, b)
"""

import random
# to generate a "pseudo" random int in the range [1,100]
secret=random.randint(1,100)
print(secret) # just for testing purpose :-) !

currentNumberOfAttempts=0

while currentNumberOfAttempts < 6:
    
    # Thanks to the following while loop the script is able to prompt the user
    # for a new value as long as the one given is not a valid int
    while True:
        try:
            currentValue=input(f"Enter an int in the range [1,100] ({currentNumberOfAttempts+1}/6): ")
            currentValue=int(currentValue)
            break
        except ValueError as ex:
            print(f"The value '{currentValue}' is not a valid int !")
            print("Please enter another value.")

    if currentValue == secret:
        print ("Bingo ! You've found the secret number")
        break
    elif currentValue > secret:
        print("Too large !")
    #elif currentValue < secret:
    else:
        print("Too small !") 
        
    #currentNumberOfAttempts = currentNumberOfAttempts + 1
    currentNumberOfAttempts += 1 # -= *= /= .....
    
    
if secret != currentValue:
    print("The secret number was:", secret)
    print(f"The secret number was: {secret}")