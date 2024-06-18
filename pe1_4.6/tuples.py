# creating and using tuples

def main():
    programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials", "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")

    for classes in programming_classes:
        print(classes, end = " ")

    print(f"There are {len(programming_classes)} classes in a tuple.")
    print("\n\n")
    print(programming_classes)

main()