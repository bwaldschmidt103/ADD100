"""
1. Define a Pet Class:
Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
Set a default value for pet_type as "Dog".
Implement getter and setter methods for all properties.
Include a class variable vet_name set to the name of your veterinary office.
Add a method display_pet_info to print all details of the pet and owner.

2. Create Pet Objects:
Instantiate at least three pet objects with different details.
Show the use of setter methods for at least one pet object.

3. Implement Property Existence Check:
Write a function check_property that uses hasattr() to verify if a property exists in a pet object.

4. Display Information:
Use display_pet_info to print details for each pet.
Show examples of check_property being used on various properties and pets.
"""

# Class definition
class Pet:
    # Class variable
    veterinary_office = "Healing Paws"

    # Initializer with private variables
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type


    # Getter and Setter for properties
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name

    def get_pet_id(self):
        return self.__pet_id
    
    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id
        
    def get_pet_name(self):
        return self.__pet_name
    
    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def get_pet_type(self):
        return self.__pet_type
    
    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type



    # Method to print pet and owner details
    def print_pet_details(self):
        print(f"Pet Details for {self.__pet_name}:")
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Type: {self.__pet_type}")  
        print(f"Veterinary Office: {Pet.veterinary_office}\n")

# Creating Pet objects
def create_pet_info():
    pet1 = Pet("Alan", "Watkins", "W32458234", "Floppy")
    print("\n\n\n")
    pet2 = Pet("Martha", "Bellview", "T324245", "Princess")
    print("\n\n\n")
    pet3 = Pet("Grace", "Tomkins", "J3252345", "Macy")
    print("\n\n\n")
    pet4 = Pet("Mark", "Wahlburg", "E34564564", "Doc")
    print("\n\n\n")    
    return pet1, pet2, pet3, pet4

# Implementing property existence check
def check_property(obj, prop):
    return hasattr(obj, prop)
                   
# Main function to demonstrate usage of the Pet class
def main():
    # Creating Pet objects
    pet1, pet2, pet3, pet4 = create_pet_info()

    # Display pet information
    pet1.print_pet_details()
    pet2.print_pet_details()
    pet3.print_pet_details()
    pet4.print_pet_details()

    # Check property existence
    print(f"Does pet1 have a pet type property? {check_property(pet1, '_Pet__pet_type')}")
    print(f"Does pet2 have a pet id property? {check_property(pet2, '_Pet__pet_id')}")
    print(f"Does pet3 have a pet name property? {check_property(pet3, '_Pet__pet_name')}")
    print(f"Does pet4 have a pet toy property? {check_property(pet4, '_Pet__pet_toy')}")

if __name__ == "__main__":
    main()

