# static guess
NUMBER = 8

# prompts the user for an integer between 1 and 10
guess = int(input("Guess a number between 1 and 10"))

# tells the user if they were higher, lower, out of bounds, or if they were correct
if guess > NUMBER:
    print("You guessed too high, try again!")
elif guess < NUMBER:
    print("You guessed too low, try again!")
elif guess < 1 or guess > 10:
    print("Please input a number between 1 and 10!")
else:
    print("You got it!")
