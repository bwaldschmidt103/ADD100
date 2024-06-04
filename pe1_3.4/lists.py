# List of days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Initialize an empty list to store steps
steps = [] 

#Loop through each day and ask the user for input
for day in days:
    steps_taken = int(input(f"How many steps did you take on {day}? ")) #Placeholder for user input
    steps.append(steps_taken) #Append the user's input

    
#Displays the steps recorded for each day
for i, day in enumerate(days):
    print(f"Steps taken on {day}: {steps[i]}")


#Calculates the total number of steps taken in the week
total_steps = sum(steps)
print() #Adds an empty space 
print(f"Total steps taken in the week: {total_steps}")


#Calculate the average steps taken
average_steps = round(total_steps / len(steps))
print(f"Average steps taken: {average_steps}")



