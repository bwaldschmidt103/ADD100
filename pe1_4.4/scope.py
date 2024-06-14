# Conversion variables (global and constant)
POUNDS_TO_KILOGRAMS = 0.453592
INCHES_TO_METERS = 0.0254

# Main function
def main():
    while True:
        # Input: Ask the user for weight and height
        weight_pounds = float(input("Enter your weight in pounds: "))
        height_inches = float(input("Enter your height in inches: "))

        # Check for negative entries
        if weight_pounds < 0 or height_inches < 0:
            print("Invalid entry. Weight and height must be positive numbers. Please try again.")
            continue

        # Conversion to Metric: Convert weight and height to metric units
        weight_kg = weight_pounds * POUNDS_TO_KILOGRAMS
        height_m = height_inches * INCHES_TO_METERS

        # BMI Calculation: Calculate BMI using the metric units
        bmi = weight_kg / (height_m ** 2)

        # BMI Categories: Determine the BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        # Output: Display the calculated BMI and category
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are in the category: {category}")
        break

# Call the main function directly
main()
