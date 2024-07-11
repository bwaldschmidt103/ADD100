'''
(1) Create the Pet Class:
Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
Implement get and set methods for each of these attributes.
Add a method called print_details that prints the details of the pet.

(2) Create Instances:
Create three objects of the Pet class with different kinds, breeds, and names.

Call the print_details method for each object that you created

(3) Demonstrate a Special Method or Function:
Choose one of the following and demonstrate its use with the Pet class instances:

__name__: Display the name of the class.
type(): Show the class used to instantiate a pet object.
__module__: Return the module name in which the Pet class is defined.
__bases__: Display the base classes of the Pet class (if any).
getattr(): Use it to access an attribute of a Pet instance.
isinstance(): Check if an instance is of the Pet class.
'''

# Defining a Pet Class
class Pet:

    # Initializer with private variables
    def __init__(self, kind, breed, name):
        # Instance variables
        self.__kind = kind
        self.__breed = breed
        self.__name = name

# Getter and Setter for properties
    def get_kind(self):
        return self.__kind
    
    def set_kind(self, kind):
        self.__kind = kind
    
    def get_breed(self):
        return self.__breed
    
    def set_breed(self, breed):
        self.__breed = breed

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    # Method to print pet details
    def print_pet_details(self):
        print(f"Pet Kind: {self.__kind}")
        print(f"Pet Breed: {self.__breed}")  
        print(f"Pet Name: {self.__name}")

# Creating Instances
def create_pet_info():
    pet1 = Pet("Cat", "Persian", "Jenna")
    print("\n\n\n")
    pet2 = Pet("Cat", "Chartreux", "Patch")
    print("\n\n\n")
    pet3 = Pet("Cat", "Himalayan", "Slinky")
    print("\n\n\n")
    pet4 = Pet("Dog", "French Bulldog", "Ace")
    print("\n\n\n")
    pet5 = Pet("Dog", "Basset Hound", "Jewels")
    print("\n\n\n")
    pet6 = Pet("Dog", "Labrador Retriever", "Chamberlain")
    print("\n\n\n")
    pet7 = Pet("Guinea Pig", "Cuy", "Pete")
    print("\n\n\n")
    pet8 = Pet("Guinea Pig", "Texel", "Sunshine")
    print("\n\n\n")
    pet9 = Pet("Guinea Pig", "Peruvian", "Oz")
    print("\n\n\n")
    pet10 = Pet("Bunny", "Havana", "Homer")
    print("\n\n\n")    
    pet11 = Pet("Bunny", "Florida White", "Budda")
    print("\n\n\n")  
    pet12 = Pet("Bunny", "Velveteen", "Zoey")
    print("\n\n\n")  
    return pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10, pet11, pet12

# Main function to demonstrate usage of the Pet class
def main():
    # Creating Pet objects
    pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10, pet11, pet12 = create_pet_info()

    # Display pet information
    pet1.print_pet_details()
    print("\n")  
    pet2.print_pet_details()
    print("\n")  
    pet3.print_pet_details()
    print("\n")  
    pet4.print_pet_details()
    print("\n")  
    pet5.print_pet_details()
    print("\n")  
    pet6.print_pet_details()
    print("\n")  
    pet7.print_pet_details()
    print("\n")  
    pet8.print_pet_details()
    print("\n")  
    pet9.print_pet_details()
    print("\n")  
    pet10.print_pet_details()
    print("\n")  
    pet11.print_pet_details()
    print("\n")  
    pet12.print_pet_details()
    print("\n")  
    
    # Demonstrating a Special Method or Function:
    print(f"Class name: {Pet.__name__}")
    print(f"Type of pet3: {type(pet3)}")
    print(f"Module name: {Pet.__module__}")
    print(f"Base classes: {Pet.__bases__}")
    print(f"Pet6 Breed: {pet6.get_breed()}")
    print(f"Is pet9 an instance of Pet? {isinstance(pet9, Pet)}")

if __name__ == "__main__":
    main()

