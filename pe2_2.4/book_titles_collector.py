def main():
    counter = 0
    max_count = 10
    titles = []

    while True:
        try:
            user_input = input("Please enter a book title: ")
            title = user_input.title()

            # Check if the title contains only spaces
            if not title.strip():
                print("Invalid Input. Please enter a valid book title.")
                continue
            
            titles.append(title)
            counter += 1

            if counter < max_count:
                continue
            else:
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid book title.")
    
    # Sort the titles alphabetically
    titles.sort()
        
    # Print the sorted titles
    print("Sorted book titles:")
    for t in titles:
        print(t)

# Calling the main function
main()

