import random

# i'm just getting fancy here, you don't need to go through all this effort if you don't need too
import sys

# the random module has lots of functions, so as long
# as you got the same output, the specific implementation
# of the program doesn't have to match mine exactly.

# rollDie() finds a random number between 1 and 6 and returns it
def rollDie():
    num = random.randint(1, 6)
    return num

# flipCoin() gets either a 1 or a 2 and interprets it into Heads or Tails, respectively, then returns
# the result
def flipCoin():
    num = random.randint(1, 2)
    if num == 1:
        return 'Heads'
    else:
        return 'Tails'

# cx
print("Choose on of the two options: ")
print("1. Roll a Die")
print("2. Flip a Coin")

# if you want to learn try-except, awesome, but it is by no means required in your solution.
try:
    choice = int(input("Your choice (1/2): "))
except:
    # if they type something that can't be converted into an int, display an error message and exit with no exceptions or errors
    print("Please input a '1' or a '2'.")
    sys.exit(0)

# runs the associated function with the user's input or asks to answer differently
if choice == 1:
    print("You rolled a " + str(rollDie()) + "!")
elif choice == 2:
    print("You got " + flipCoin() + "!")
else:
    print("Please input a '1' or a '2'.")

