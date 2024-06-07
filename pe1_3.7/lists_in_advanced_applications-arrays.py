# Define the time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# Initialize an empty list to store heart rate data
heart_rates = []

# Initialize a variable to keep track of the total heart rate
total_heart_rate = 0

# Iterate over each time slot
for time_slot in time_slots:
    # Ask the user to enter their heart rate for the current time slot
    heart_rate = int(input(f"Enter your heart rate (in bpm) for {time_slot}: "))
    
    # Append the time slot and heart rate to the heart_rates list
    heart_rates.append([time_slot, heart_rate])
    
    # Add the heart rate to the total
    total_heart_rate += heart_rate

# Calculate the average heart rate
average_heart_rate = total_heart_rate / len(time_slots)

# Print the average heart rate
print(f"The average heart rate is: {average_heart_rate} bpm")


