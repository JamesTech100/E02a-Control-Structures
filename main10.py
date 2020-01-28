#!/usr/bin/env python3
import sys, random #importing necessary libraries

assert sys.version_info >= (3,7), "This script requires at least Python 3.7" #requiring the version of of python to be newer than 3.7


print('Greetings!') #prints a friendly message!
colors = ['red','orange','yellow','green','blue','violet','purple'] #defines a list of colors
play_again = '' #sets play_again to a null value
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): # keeps looping as long as the user agrees to play again
    match_color = random.choice(colors) #
    count = 0 # sets attempt count to 0
    color = '' # random color is set to null value
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()
        count += 1
        if (color == match_color):
            print('Correct!')
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    print('\nYou guessed it in {} tries!'.format(count))

    if (count < best_count):
        print('This was your best guess so far!')
        best_count = count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

print('Thanks for playing!')