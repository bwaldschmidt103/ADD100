"""
Assignment Part 1: Defining Classes
File 1: Write an Employee class with the following attributes:

Employee name
Employee number
Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:

Shift number (integer: 1 for day, 2 for night)
Hourly pay rate
Implement accessor and mutator methods (getters and setters) for each class.

Assignment Part 2: Implementing and Testing
 

Part 2: Write a script to:

Create an instance of ProductionWorker.
Prompt the user for each attribute's data.
Store and then display the data using the object's methods.
"""

# Defining Classes
class Employee:
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number

class Production_Worker(Employee):
    def __init__(self, employee_name, employee_number, hourly_pay_rate, shift_number):
        super().__init__(employee_name, employee_number)
        self.hourly_pay_rate = hourly_pay_rate
        self.shift_number = shift_number
        

    # Getter and Setter for each class
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
    
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number
    
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def __str__(self):
        return f"Enter the following details of the Employee\n" \
               f"--------------------------------------------\n" \
               f"Enter Employee Name: {self.employee_name}\n" \
               f"Enter Employee Number: {self.employee_number}\n" \
               f"Enter Pay Rate: {self.hourly_pay_rate}\n" \
               f"Enter Shift Number: {self.shift_number}\n" \
               f"-------------------------------------------------------\n" \
               f"Details of Employee:\n" \
               f"-------------------------------------------------------\n" \
               f"Name: {self.employee_name}\n" \
               f"Employee Number: {self.employee_number}\n" \
               f"Shift: {'Night' if self.shift_number == '2' else 'Day'}\n" \
               f"Pay Rate: {self.hourly_pay_rate}"

# # Main function to demonstrate instances of Production workers
def main():
    
    print("\n")
    bobby = Production_Worker ("Bobby", "908241", "24.00", "2")
    print(bobby)

    print("\n")
    marco = Production_Worker ("Marco", "234576", "22.50", "2")
    print(marco)

    print("\n")
    suzanne = Production_Worker ("Suzanne", "425245", "18.00", "1")
    print(suzanne)

    print("\n")
    justine = Production_Worker ("Justine", "987234", "26.00", "1")
    print(justine)

if __name__ == "__main__":
    main()

