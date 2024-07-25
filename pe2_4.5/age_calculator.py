"""
In this assignment, you will create a program that asks the user for their birthday and then calculates their age in different units such as years, months, days, hours, and minutes. This exercise will help you practice using the datetime and timedelta modules in Python.

Assignment Objectives:
Ask the user to input their birthday.
Calculate the user's age in years, months, days, hours, and minutes.
Provide detailed comments to all of the code, explaining what each line that has to do with time calculation does.
Display the results in a user-friendly format.
Implement the solution inside a main() function.
Instructions:
Create a Python script that performs the following steps:

Define a main() function where your program logic will reside.
Use my start program from GitHub: startprogramLinks to an external site.
You can view the classroom demonstration of how we got to the code at the top of the page.
Comment explaining each line of the code
Finish the code to get and display:
months
weeks
days (done)
years (done)
Format and print the results in a clear, understandable manner.
Tips:
To calculate the age in years, you might need to consider leap years. A simple approach is to divide the total number of days by 365.25.
For months, first calculate the years, then use the remaining days to estimate the months.
For weeks, calculate by dividing days by 7
Use try-except blocks to handle any potential input errors.
"""

import datetime

def get_user_birthday():

    # Get the user's birthday as an input and return a datetime object.
    while True:
        try:
            birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
            birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d")
            return birthday
        except ValueError:
            print("Invalid date format. Please enter your birthday in YYYY-MM-DD format.")

def calculate_age(birthday):
    
    # Calculate age using
    today = datetime.datetime.now()
    age = today - birthday

    # Calculate years, months, and days
    years = age.days // 365
    remaining_days = age.days % 365
    months = remaining_days // 30
    days = remaining_days % 30

    return years, months, days, age

def display_age(years, months, days, birthday, age):
    
    # Display the age and additional information.
    print(f"What year were you born? {datetime.datetime.now().year - years}")
    print(f"What Month were you born (as a number)? {birthday.month}")
    print(f"What day of the month were you born? {birthday.day}")
    print(f"Your birthday is: {birthday.strftime('%B %d, %Y')}")
    print(f"Difference is {age.days} days")
    print(f"You are {years} years old")

def main():
    birthday = get_user_birthday()
    if birthday:
        years, months, days, age = calculate_age(birthday)
        display_age(years, months, days, birthday, age)

if __name__ == "__main__":
    main()

