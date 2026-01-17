import random


def number_guessing_game():
    

    secret_number = random.randint(1, 100)
    
    guesses_taken = 0
    game_won = False
    
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    while not game_won:
        guess_input = input("Enter your guess: ")
        
        try:
            guess = int(guess_input)
            
            guesses_taken += 1
            
            if guess == secret_number:
                game_won = True
                print(f"Good job! You guessed my number in {guesses_taken} guesses!")
            elif guess < secret_number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
