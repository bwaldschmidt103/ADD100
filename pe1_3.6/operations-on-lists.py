def display_available_seats(seats):
    print("Available seats:", seats)

def sell_ticket(seats):
    while True:
        seat_number = input("Enter the seat number you want to purchase (1-20), or '0' to finish: ") 
        if seat_number.isdigit():
            seat_number = int(seat_number)
            if seat_number == 0:
                break
            elif seat_number not in seats:
                print("This seat is either sold or does not exist. Please choose a different seat.")
            else:
                seats.remove(seat_number)
                print(f"Seat {seat_number} has been successfully sold.")
                display_available_seats(seats)
        else:
            print("Please enter a valid seat number.") 

def main():
    # Initialize the seating list
    available_seats = list(range(1, 21))

    # Display available seats
    display_available_seats(available_seats)

    # Implement the ticket purchase process
    sell_ticket(available_seats)

    # Final list of available seats after sales
    print("Final list of available seats:")
    display_available_seats(available_seats)

# Run the main function
if __name__ == "__main__":
    main()
    