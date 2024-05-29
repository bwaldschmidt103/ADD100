# Calculating numeric grade to letter grade

numeric_grade = int(input("Please enter your numeric grade: "))

# Initialize grade variable
grade = ''

# Check if numeric grade is within the valid range
if numeric_grade < 0 or numeric_grade > 100:
    print("Please enter a number between 0 and 100.")
else:
    if numeric_grade < 60:
        grade = 'F'
    elif numeric_grade < 70:
        grade = 'D'
    elif numeric_grade < 80:
        grade = 'C'
    elif numeric_grade < 90:
        grade = 'B'
    elif numeric_grade <= 100:  # Changed from < 100 to <= 100
        grade = 'A'
    
    print("The letter grade is:", grade)
    