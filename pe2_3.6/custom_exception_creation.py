"""
Objective
Create a custom exception class to handle a specific error scenario in a Python program.

Task
Define a new exception class named NotNumericError that inherits from the base Exception class. This exception should be raised when a user inputs an invalid value in a simple input-validation program. Your program should prompt the user to enter a number and raise the NotNumericError if the input is not a number.

Requirements
Implement a custom exception class NotNumericError.
Write a Python script that prompts the user to input a number.
Use a try-except-else-finally block:
The try block should contain the logic to check if the input is a number. (isnumeric() )
The except block should catch the NotNumericError and print an error message.
The else block should print a confirmation message if the input is valid.
The finally block should print a message indicating the end of the program's execution.
Ensure the program gracefully handles the exception and continues to prompt the user until a valid number is entered. (call the program again)
 """


class NotNumericError(Exception):
    # Custom exception implementation
    pass

def main():
    while True:
        try:
            # Prompt for user input and validate
            number = input("Please enter a number: ")
            if not number.isnumeric():
                raise NotNumericError("Invalid input, please enter a valid number")  
        except NotNumericError as e:
            # Handle invalid input
            print(e)
        else:
            # Confirm valid input
            print("The entry is valid")
            break # Exit the loop if input is valid
        finally:
            # Indicate end of this iteration
            print("This is the end of the program")

if __name__ == "__main__":
    main()

