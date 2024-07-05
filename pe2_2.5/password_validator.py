""""
Set up your program in a main() function
Create a Python program that asks the user to input a password.
Ensure the password meets the following criteria:
Between 8 to 20 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Includes at least one number.
Includes at least one symbol from the set: !@#$%&*.
Use a while loop to keep asking for the password until all criteria are met.
Once a valid password is entered, prompt the user to enter it again for confirmation.
Use try-except blocks to handle any errors or exceptions that occur.
If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.
"""


def main():
    valid = False # change to true if all conditions are met
    while not valid:
        valid = True # we will change to false if ANY requirements are not met
        print("""Password Requirements:\n
            Between 8 to 20 characters long.\n
            Contains at least one uppercase letter.\n
            Contains at least one lowercase letter.\n
            Includes at least one number.\n
            Includes at least one symbol from the set: !@#$%&*\n""")

        password = input("Please enter a password that meets the criteria: ")
        length = len(password)

        if not (7 <= length <= 20):
            valid = False
            print("That password is not the right length")

        is_upper = False # change to true if found
        is_lower = False # change to true if found
        for char in password: # for loop stepping through characters in password. 
            if char.isupper(): # Look for an upper case.
                is_upper = True
            elif char.islower(): # Look for a lowercase letter.
                is_lower = True
 
        has_symbol = False
        symbol = ['!', '@', '#', '$', '%', '&', '*']
        for char in password:
            if char in symbol:
                has_symbol = True
                break
               

        if not (is_upper and is_lower and has_symbol):
            print("you need to include an uppercase letter, a lowercase letter, and a symbol")
            valid = False
            
    print("Password is valid!")


main()
