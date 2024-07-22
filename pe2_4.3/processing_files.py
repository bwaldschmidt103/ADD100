"""
Open the file sales_totals in read mode (Download: sales_totals.txt Download sales_totals.txt)
Read in all the lines using a loop
Strip the newline symbol and convert each line to a float
Add each number to the running total
Count the number of lines
Format and display each number
Outside of the loop, format and display the total, the count, and the average
Do this using a main function 
Use try and except statements to handle file errors
"""

import os

def main():
    try:
        # Obtain the absolute file path
        path = os.path.abspath(r'C:\z_admin\School\Assignments\add100\python\pe2_4.3\sales_totals.txt')

        # Open the file in read mode        
        with open(path, 'r') as file:
            total = 0.0
            count = 0

            # Read each line and process the data
            for line in file:
                try:
                    # Convert the line to a float and add it to the total
                    sale = float(line.strip())
                    total += sale
                    count += 1
                    print(f"Sale {count}: ${sale:.2f}")
                except ValueError:
                    print(f"Error: Invalid sale amount in line {count + 1}")

            # Calculate the average
            if count > 0:
                average = total / count
                print(f"\nTotal sales: ${total:.2f}")
                print(f"Number of sales: {count}")
                print(f"Average sale: ${average:.2f}")
            else:
                print("No valid sales data found in the file.")

    except FileNotFoundError:
        print("Error: File 'sales_totals.txt' not found.")

if __name__ == "__main__":
    main()

