print("This is a number guessing game")
x = input("Enter your name: ").title() #.title() converts first character in each word into upper case.
print(f"Dear,{x}. Let's play the game.")
import random #random module, which provides functions for generating random numbers,needed for the game logic. 
random_number = random.randrange(1,10) #assigns a random integer from 1 to 9 to the variable random_number. 
guess = int(input("What could be the number between 0 to 10? "))
correct = False #It assigns the boolean value False to the variable correctand checks whether user guessed correct or not.
print(random_number)

while not correct: #starts a while loop that repeats until the value of correct(variable) is True. This is the main loop of the game.
    if guess==random_number:
        print("Congrats you got it")
        correct = True  #assigns the boolean value True to the variable correct. This is to stop the loop and end the game.
    elif guess>random_number:
        print("Your guess is high")
        break
    elif guess<random_number:
        print("Your guess is low")
        break
    else:  # An else clause handles cases not covered by the previous conditions. This is unlikely to happen, but it is good practice to use .
        print("Try something else")
        break #This statement exits the loop immediately. This is to stop the game after one guess.