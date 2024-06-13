# Define the function calculate_interest
def calculate_interest(principal, rate, time):
    # Calculate the simple interest using the formula
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Prompt the user for input
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (as a whole number): "))
investment_time = float(input("Enter the investment time in years (as a whole number): "))


# Call the function and pass the information in
calculated_interest = calculate_interest(principal_amount, interest_rate, investment_time)


# Print the result in a user-friendly string, formatted
print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
at an interest rate of {interest_rate}% over a period of \
{investment_time} years is: ${calculated_interest:,.2f}")