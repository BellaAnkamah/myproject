import random

secret_number = random.randint(1, 100)

while True:
    user_input = input("Guess the secret number (between 1 and 100): ")
    
    try:
        guess = int(user_input)
        
        if guess < 1 or guess > 100:
            print("Error,Please enter a number between 1 and 100.")
            continue
        
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    except ValueError:
        print("Error, Please enter a valid integer between 1 and 100.")

