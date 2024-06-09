import random

def display_instructions():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 200.")
    print("Try to guess it in as few attempts as possible.")
    print("After each guess, I will tell you if your guess is too high, too low, or correct.")
    print("You may also receive some extra hints along the way!")
    print()

def give_hint(number_to_guess, guess):
    if abs(number_to_guess - guess) <= 10:
        return "You're very close!"
    elif abs(number_to_guess - guess) <= 20:
        return "You're close!"
    else:
        return "You're far off."

def main():
    print("May I ask you for your name?")
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! Let's play a game.")
    print("I am thinking of a number between 1 and 200.")
    
    display_instructions()
    
    number_to_guess = random.randint(1, 200)
    attempts = 0
    
    while True:
        guess_input = input("Go ahead. Guess: ")
        try:
            guess = int(guess_input)
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
                print(give_hint(number_to_guess, guess))
            elif guess > number_to_guess:
                print("Too high! Try again.")
                print(give_hint(number_to_guess, guess))
            else:
                print(f"Congratulations, {user_name}! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("I don't think that is a number. Sorry.")
        print()

if __name__ == "__main__":
    main()
