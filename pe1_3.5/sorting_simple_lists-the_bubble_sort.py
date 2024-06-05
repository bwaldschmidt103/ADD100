# Function to perform bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Function to accept names from the user
def accept_names():
    names = []
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        names.append(name)
    return names

# Main program
if __name__ == "__main__":
    # Accept names from the user
    names_list = accept_names()
    
    # Sort the list using bubble sort
    bubble_sort(names_list)
    
    # Print the sorted list
    print("Sorted list:", names_list)
    
    # Reverse the sorted list
    names_list.reverse()
    
    # Print the reversed sorted list
    print("Reversed sorted list:", names_list)
    