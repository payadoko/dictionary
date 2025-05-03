import random

secret_number = random.randint(1, 10)

print("Welcome to the Guess number Game")
print("Try to guess the number between 1 to 10")
guess = None

while guess != secret_number:
    guess = int(input("Enter your guess"))

    if guess > secret_number:
        print(f"{guess} is too high! Try again")

    elif guess < secret_number:
        print(f"{guess} is too low! Try again")
    else:
        print(f"Congratulations {guess} is the correct number")

        
