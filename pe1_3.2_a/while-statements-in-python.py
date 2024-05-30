count = 99
while count > 0:
    if count > 1:
        print(count, "bottles of beer on the wall")
        print(count, "bottles of beer")
        print("Take one down, pass it around")
        count -= 1 #Decrement count
        if count == 1:
            print(count, "bottle of beer on the wall!\n")
        else:
            print(count, "bottles of beer on the wall!\n")
    else:
        print(count, "bottle of beer on the wall")
        print(count, "bottle of beer")
        print("Take one down, pass it around")
        count -= 1 #Decrement count
        print("No more bottles of beer on the wall!\n")
