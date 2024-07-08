""""
    Your task is to design and implement a class in a programming language. This class will represent a person and hold personal data.
 

Assignment Steps:

Class Creation: Design a class named Person that includes the following data: name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read.
"""

# Class definition for a Person 
class Person:
    # Initializer with private variables
    def __init__(self, first_name, last_name, address, age, phone_number):
        self.__first_name = first_name      # Private variable for first name
        self.__last_name = last_name        # Private variable for last name
        self.__address = address            # Private variable for address
        self.__age = age                    # Private variable for age
        self.__phone_number = phone_number  # Private variable for phone number

    # Method to get and set a person's info as a formatted string
    def get_info(self):
        return f"{self.__first_name} {self.__last_name}, Address: {self.__address}, Age: {self.__age}, Phone Number: {self.__phone_number}"

    # Getter for first_name
    def get_first_name(self):
        return self.__first_name
    
    # Getter for last_name
    def get_last_name(self):
        return self.__last_name
    
    # Getter for address
    def get_address(self):
        return self.__address
    
    # Getter for age
    def get_age(self):
        return self.__age
    
    # Getter for phone_number
    def get_phone_number(self):
        return self.__phone_number
    
    # Setter for first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name
    
    # Setter for last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # Setter for address
    def set_address(self, address):
        self.__address = address

    # Setter for age
    def set_age(self, age):
        self.__age = age

    # Setter for phone_number
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

# Creating Instances: Write a program that creates three instances (objects) of the Person class.
def main():
    # imaginary friends 
    person1 = Person("Roger", "Sanders", "24543 Rocky Road", "44", "(863)234-7722")
    person2 = Person("Suzanne", "Alexander", "8357 Lakeland Ave", "32", "(824)679-8080")
    person3 = Person("David", "Silver", "222 Liberty St", "52", "(843)279-1766")

    # Printing out the store information
    print("\n\n\n\n\n")
    print(person1.get_info())
    print(person2.get_info())
    print(person3.get_info())
    print("\n\n\n\n\n")

main()

