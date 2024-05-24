# This program calculates one's total budget and divides it by each living expense then converting it into a percentage of the total budget.
total_budget = float(input("Enter the total_budget: "))
rent_mortgage = float(input("Enter the rent_mortgage: "))
utilities = float(input("Enter the utilites: "))
groceries = float(input("Enter the groceries: "))
transportation = float(input("Enter the transportation: "))
health_care = float(input("Enter the health_care: "))
personal_care = float(input("Enter the personal_care: "))
clothing = float(input("Enter the clothing: "))
debt = float(input("Enter the debt: "))

print("\n")

print(f"The rent or mortgage utilized from the total budget is {rent_mortgage / total_budget * 100:.2f}%.") #outputs the rent or mortgage percentage of the total budget
print (f"The utilities utilized from the total budget is {utilities / total_budget * 100:.2f}%.") #outputs the utilities percentage of the total budget
print (f"The groceries utilized from the total budget is {groceries / total_budget * 100:.2f}%.") #outputs the groceries percentage of the total budget
print (f"The transportation utilized from the total budget is {transportation / total_budget * 100:.2f}%.") #outputs the transportation percentage of the total budget
print (f"The health care utilized from the total budget is {health_care / total_budget * 100:.2f}%.") #outputs the health care percentage of the total budget
print (f"The personal care utilized from the total budget is {personal_care / total_budget * 100:.2f}%.") #outputs the personal care percentage of the total budget
print (f"The clothing utilized from the total budget is {clothing / total_budget * 100:.2f}%.") #outputs the clothing percentage of the total budget
print (f"The debt utilized from the total budget is {debt / total_budget * 100:.2f}%.") #outputs the debt percentage of the total budget