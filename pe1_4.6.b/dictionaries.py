def main():
    # A Python program using a dictionary to translate letters into NATO Phonetic Alphabet
    nato_dictionary = {
        "A": "Alpha", "B": "Bravo", "C": "Charlie",
        "D": "Delta", "E": "Echo", "F": "Foxtrot",
        "G": "Golf", "H": "Hotel", "I": "India", 
        "J": "Juliette", "K": "Kilo", "L": "Lima", 
        "M": "Mike", "N": "November", "O": "Oscar",
        "P": "Papa", "Q": "Quebec", "R": "Romeo", 
        "S": "Sierra", "T": "Tango", "U": "Uniform",
        "V": "Victor", "W": "Whiskey", "X": "X-Ray", 
        "Y": "Yankee", "Z": "Zulu"
    }
    
    # Developing Spelling Program
    def spell_word():
        user_word = input("Enter a word: ")
        spelled_word = ""
        for index, letter in enumerate(user_word.upper()):
            if letter in nato_dictionary:
                spelled_word += nato_dictionary[letter]
                if index < len(user_word) -1: # Check if it's not the last letter
                    spelled_word += " " # Add a space after the NATO word
        return spelled_word

    # Call the spell_word function to execute the spelling program
    print(spell_word())

main()
    