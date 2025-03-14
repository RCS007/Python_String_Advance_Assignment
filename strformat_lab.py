# Task One
# Given tuple
data = (2, 123.4567, 10000, 12345.67)

# Using format string
formatted_string = "file_{:03d} : {:8.2f}, {:.2e}, {:.3e}".format(data[0], data[1], data[2], data[3])
print(formatted_string)

# Task Two
# Using f-strings
formatted_fstring = f"file_{data[0]:03d} : {data[1]:8.2f}, {data[2]:.2e}, {data[3]:.3e}"
print(formatted_fstring)

# Task Three
# Given tuple
date_tuple = (4, 30, 2017, 2, 27)

# Reordering and formatting
formatted_date = "{:02d} {:02d} {} {:02d} {:02d}".format(date_tuple[3], date_tuple[4], date_tuple[2], date_tuple[0], date_tuple[1])
print(formatted_date)

# Task Four
# Given list
fruits = ['oranges', 1.3, 'lemons', 1.1]

# Using f-strings
formatted_fruits = f"The weight of an {fruits[0]} is {fruits[1]} and the weight of a {fruits[2]} is {fruits[3]}"
print(formatted_fruits)

# Modified to uppercase fruit names and increased weight by 20%
formatted_fruits_upper = f"The weight of an {fruits[0].upper()} is {fruits[1] * 1.2:.2f} and the weight of a {fruits[2].upper()} is {fruits[3] * 1.2:.2f}"
print(formatted_fruits_upper)

# Task Five
# Displaying a table with name, age, and cost
table_data = [
    ("Alice", 25, 99.01),
    ("Bob", 30, 150.75),
    ("Charlie", 35, 1025.50),
    ("David", 40, 9999.99)
]

# Formatting the table
print("\n{:<10} {:<10} {:<10}".format("Name", "Age", "Cost"))
for name, age, cost in table_data:
    print("{:<10} {:<10} ${:<10,.2f}".format(name, age, cost))

# Extra Task: Printing a tuple in columns 5 characters wide
numbers = tuple(range(1, 11))
print("\n" + " ".join(f"{num:5}" for num in numbers))
