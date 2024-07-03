""""
Create a Main Function: Encapsulate your program within a main() function.
User Input for Flower List: Prompt the user to enter names of flowers and store them in a list. Have them enter the word "done" when done, and check for it.
Sorting and Searching: Sort the list, print on screen with a number next to the flower name, and allow the user to search for a specific flower. Print a message if the flower is found.
Accessing a Specific Flower: Ask the user for a number to access the corresponding flower. Handle errors for invalid inputs. (Note, our printout starts at 1, list indexes start at 0, adjust accordingly.
Exception Handling: Use try and except statements for ValueError and IndexError, and include a generic except statement.
"""

def main():
    try:
        # Initialize an empty list of store flowers
        flowers = []

        # Prompt the user to enter flower names      
        print("Please enter flower names (type 'done' when finished):")
        while True:
            flower = input("Enter a flower name: ")
            if flower.lower() == 'done':
                break
            flowers.append(flower)

        # Sort the list of flowers
        flowers.sort()

        # Print the sorted list with numbers
        print("\nList of flowers:")
        for i, flower in enumerate(flowers, start=1):
            print(f"{i}. {flower}")

        # Print the entire list of flowers
        print("List of flowers:", flowers)

        # Ask the user to search for a specific flower
        search_flower = input("\nEnter a flower name to search: ")
        if search_flower in flowers:
            print(f"{search_flower} is found in the list.")
        else:
            print(f"{search_flower} is not found in the list.")

        # Ask the user for a number to access a specific flower
        try:
            index = int(input("\nEnter a number to access the corresponding flower: ")) -1
            if 0 <= index < len(flowers):
                print(f"Flower at index {index + 1}: {flowers[index]}")
            else:
                print("Invalid input. Please enter a valid number.")                        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Index out of range. Please enter a valid number.")

    except Exception as e:
        print(f"An error occurred {e}")


if __name__ == "__main__":
    main()

