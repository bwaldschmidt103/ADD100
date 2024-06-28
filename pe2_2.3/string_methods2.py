# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
# Your code here
x = string1.capitalize()
print(x)
print()

# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> "  python  "
string2 = "python is fun"
# Your code here
x = string2.center(30)
print(x)
print()

# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
# Your code here
x = string3.endswith("on")
print(x)
print()

# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
# Your code here
x = string4.find("th")
print(x)
print()

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
# Your code here
x = string5.isalnum()
print(x)
print()

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
# Your code here
x = string6.isalpha()
print(x)
print()

# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "PYTHON"
# Your code here
x = string7.islower()
print(x)
print()

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if "   " is all whitespace
string8 = "   "
# Your code here
x = string8.isspace()
print(x)
print()

# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
# Your code here
x = string9.isupper()
print(x)
print()

# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
# Your code here
x = "-".join(iterable1)
print(x)
print()

# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "MONTY PYTHON"
# Your code here
x = string10.lower()
print(x)
print()

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from "  python"
string11 = "  Monty Python"
# Your code here
x = string11.lstrip()
print("Of all the TV shows that I like,", x, "is my favorite")
print()

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python  "
string12 = "pizza  "
# Your code here
x = string12.rstrip()
print(x)
print()

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
# Your code here
x = string13.replace("python", "pizza")
print(x)
print()

# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
# Your code here
x = string14.rfind("on")
print(x)
print()

# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
# Your code here
x = string15.split()
print(x)
print()

# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
# Your code here
x = string16.startswith("py")
print(x)
print()

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from "  python  "
string17 = "  python  "
# Your code here
x = string17.strip()
print(x)
print()

# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
# Your code here
x = string18.swapcase()
print(x)
print()

# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
# Your code here
x = string19.title()
print(x)
print()

# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
# Your code here
x = string20.upper()
print(x)
