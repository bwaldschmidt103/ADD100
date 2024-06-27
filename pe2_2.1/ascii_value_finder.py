def main():
    user_input = input("Enter a character: ")

    # Initialize ascii_value
    ascii_value = None

    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")
        if len(user_input) > 1:
            print("The loop will continue until you enter exactly one character.")

    # Assign the ASCII value after the loop if it hasn't been assigned yet
    if ascii_value is None:
        ascii_value = ord(user_input)
    
    print(f"The ASCII value of {user_input} is {ascii_value}")

main()

