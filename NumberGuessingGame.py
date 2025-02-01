import random
lower_bound = 1
upper_bound = 1000
max_attempts = 10

number = random.randint(lower_bound, upper_bound)

def get_guess():
    while True:
        try:
            guess = int(input(f"\nGuess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_guess(guess, number, prev_diff=None):
    diff = abs(guess-number)
    if guess == number:
        return "Correct!", diff
    hint = "Too low!" if guess < number else "Too high!"
    if prev_diff is not None:
        if diff > prev_diff:
            hint += " You're getting farther away! 😞"
        elif diff < prev_diff:
            hint+= " But you're getting closer! 🥳"
        else:
            hint += " You're the same distance away."
    return hint, diff
    
def play_game():
    attempts=0
    won = False
    prev_diff = None
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result, prev_diff = check_guess(guess, number, prev_diff)
        if result == "Correct!":
            print(f"Congratulations! You guessed the secret number {number} in {attempts} attempts! 🥳\n")
            won = True
            break
        else:
            print(f"{result}. Try again!")
    if not won:
        print(f"You ran out of attempts :( \nThe secret number is {number}\n")

if __name__ == "__main__":
    print("\nWelcome to the Number Guessing Game!")
    play_game()