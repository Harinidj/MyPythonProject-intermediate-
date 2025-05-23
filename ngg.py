import random

def guess_number():
    print("THE GAME STARTS")
    print("Think of a number between 1 and 100.")
    print("I'll try to guess it.")
    
    low = 1
    high = 100
    
    attempts = 0
    
    while True:
        guess = random.randint(low, high)
        attempts += 1

        print(f"\nMy guess: {guess}")
        
        response = input("Is your number (h)igher, (l)ower, or (c)orrect? ").lower()
        
        if response == "h":
            low = guess + 1
        elif response == "l":
            high = guess - 1
        elif response == "c":
            print(f"\nYay! I guessed it in {attempts} attempts.")
            break
        else:
            print("Invalid input. Please respond with 'h', 'l', or 'c'.")

if __name__ == "__main__":
    guess_number()
