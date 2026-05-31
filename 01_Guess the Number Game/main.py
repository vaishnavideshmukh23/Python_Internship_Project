print('''
                         | |                  
 _ __  _   _ _ __ ___ | |__   ___ _ __ ___ 
| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__/ __|
| | | | |_| | | | | | | |_) |  __/ |  \__ \
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|  |___/
''')

#Welcome to the "Number Guessing Game" !
import random
print("WELCOME TO THE GUESS THE NUBMER GAME !")
print("Guess the number between 1 to 100 ?")
#Applied outer loop
while True:
    secret_number = (random.randint(1, 100))
    attempts = 5
    win = False
    #Inner loop
    while attempts > 0:
        #Gives input to the user
        user_guess = int(input("Enter your guess ?\n"))
        #Applied if else statement
        if user_guess == secret_number:
            print("Correct!! You guessed the number.")
            win = True
            break
        elif user_guess < secret_number:
            attempts -= 1
            print("Too low ")
        else:
            attempts -= 1
            print("Too high")
            #Applied nesetled if statement
            if attempts > 0:
                print(f"Attempts left: {attempts}")
    if not win and attempts == 0:
        print(f"Game Over ! The number was :{secret_number}")
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing")
        break


