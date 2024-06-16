# Defining Function named Factorial

def factorial(n):
    # Base case: if n is 1 or 0, return 1
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        # Recursive case: multiply n by the factorial of n-1
        return n * factorial(n-1)

        
def main():
    integer = int(input("Enter a non-negative integer: "))
    if integer < 0:
        print("Error: Input must be a non-negative integer")
        return # Exit the function if the input is invalid
    result = factorial(integer)
    # Print the result in the specified format
    print(f"The factorial of {integer} is: {result}")

# Call the main function to run the program
main()
