import random

def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    
    # Set range and attempts
    lower = 1
    upper = 50
    attempts = 5
    
    # Generate random number
    number = random.randint(lower, upper)
    
    print(f"I'm thinking of a number between {lower} and {upper}.")
    print(f"You have {attempts} attempts to guess it.\n")
    
    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempt {attempt}: Enter your guess: "))
                if lower <= guess <= upper:
                    break
                else:
                    print(f"Please enter a number between {lower} and {upper}.")
            except ValueError:
                print("Invalid input! Enter an integer.")

        if guess == number:
            print(f"🎉 Correct! You guessed the number in {attempt} attempt(s)!")
            return
        elif guess < number:
            print("Too Low! Try again.\n")
        else:
            print("Too High! Try again.\n")

    print(f"❌ Sorry! You've used all {attempts} attempts. The number was {number}.")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
