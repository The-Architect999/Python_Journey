import random

# --- THE ENGINE (This is what we will test) ---
def run_guess(guess, answer):
    """Returns True if correct, False if wrong/out-of-bounds"""
    try:
        if 0 < guess < 11:
            if guess == answer:
                return True
            else:
                return False
        else:
            return False
    except (TypeError,ValueError) as err:
        return err

# --- THE TERMINAL INTERFACE (We do not test this part) ---
if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Guess a number 1-10: '))
            if run_guess(guess, answer):
                print("You're a genius!")
                break
            else:
                print('Try again or check your limits (1-10).')
        except ValueError:
            print('Numbers only!')

