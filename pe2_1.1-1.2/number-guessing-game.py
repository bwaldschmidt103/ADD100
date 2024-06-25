import random

def main():
    # Generate a random number between 1 and 100
    actual_number = random.randint(1, 100)

    while True:
        try:
            # Get user's guess
            guess = int(input("Enter your guess (1-100): "))
            
            # Calculate the absolute difference
            difference = abs(actual_number - guess)

            # Provide feedback based on the proximity of the guess to the actual number
            if difference == 0:
                print("Congradulations! You've guessed the correct number.")
                break
            elif difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold")
        except ValueError:
            print("Please enter a valid integer.")
            
# Calling the main function
main()


