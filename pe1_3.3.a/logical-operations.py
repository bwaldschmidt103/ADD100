a = 210
b = 330
c = 195
d = 350
e = 280
f = 225
num_1 = int(input("Enter an integer: "))
num_2 = int(input("Enter another integer: "))

# and operator
result_1 = num_1 > b and num_2 > b
result_2 = num_1 > a and num_2 > a
print("Both inputs are greater than 330:", result_1)
print("Both inputs are greater than 210:", result_2)

# or operator
result_3 = num_1 < c or num_2 > d
result_4 = num_1 > c or num_2 < d
print(str(num_1) + " is less than 195 or " + str(num_2) + " is more than 350:", result_3)
print(str(num_1) + " is more than 195 or " + str(num_2) + " is less than 350:", result_4)

#not operator
result_5 = (num_1 != e)
result_6 = (num_2 != f)

print(f"{num_1} is not equal to {e}: {result_5}")
print(f"{num_2} is not equal to {f}: {result_6}")
