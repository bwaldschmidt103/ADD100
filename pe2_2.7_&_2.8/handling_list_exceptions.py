def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

    def replace_artist():
        try:
            index = int(input("Enter the index of the artist to replace (0-9): "))
            if index < 0 or index >= len(top_artists):
                raise IndexError
            new_artist = input("Enter the new artist name: ")
            top_artists[index] = new_artist
            print(f"Artist at index {index} has been replaced with {new_artist}.")
            print(top_artists) # Add this line to display the updated list
        except (ValueError, IndexError):
            print("An input error ocurred. Please enter a valid index (0-9).")

    replace_artist()

if __name__ == "__main__":
    main()
