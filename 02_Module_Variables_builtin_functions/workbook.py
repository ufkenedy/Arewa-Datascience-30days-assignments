# 
# ## 💻 Exercises - Module 2
# 
# ### Exercises: Level 1
# 
# 1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
# 3. Declare a first name variable and assign a value to it
# 4. Declare a last name variable and assign a value to it
# 5. Declare a full name variable and assign a value to it
# 6. Declare a country variable and assign a value to it
# 7. Declare a city variable and assign a value to it
# 8. Declare an age variable and assign a value to it
# 9. Declare a year variable and assign a value to it
# 10. Declare a variable is_married and assign a value to it
# 11. Declare a variable is_true and assign a value to it
# 12. Declare a variable is_light_on and assign a value to it
# 13. Declare multiple variable on one line
# 
# ### Exercises: Level 2
# 
# 1. Check the data type of all your variables using type() built-in function
# 1. Using the _len()_ built-in function, find the length of your first name
# 1. Compare the length of your first name and your last name
# 1. Declare 5 as num_one and 4 as num_two
# 1. Add num_one and num_two and assign the value to a variable total
# 1. Subtract num_two from num_one and assign the value to a variable diff
# 1. Multiply num_two and num_one and assign the value to a variable product
# 1. Divide num_one by num_two and assign the value to a variable division
# 1. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
# 1. Calculate num_one to the power of num_two and assign the value to a variable exp
# 1. Find floor division of num_one by num_two and assign the value to a variable floor_division
# 1. The radius of a circle is 30 meters.
#     1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
#     2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
#     3. Take radius as user input and calculate the area.
# 1. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# 1. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
# 
# 🎉 CONGRATULATIONS ! 🎉
# 
# [<< Module 1](../readme.md) | [Module 3 >>](../03_Module_Operators/03_operators.md)

# %%

### Exercises: Level 1


# Day 2: 30 Days of python programming

# Declare variables and assign values

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
country = "USA"
city = "New York"
age = 25
year = 2024
is_married = False
is_true = True
is_light_on = True

# Declare multiple variables on one line
x, y, z = 1, 2, 3

### Exercises: Level 2


# Check data types
print(type(first_name))

print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Find the length of the first name
print(len(first_name))

# Compare the length of first name and last name
print(len(first_name) == len(last_name))

# Arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total, diff, product, division, remainder, exp, floor_division)

# Circle calculations
radius = 30
pi = 3.14159
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print(area_of_circle, circum_of_circle)

# Take radius as user input and calculate the area
user_radius = float(input("Enter the radius of the circle: "))
user_area_of_circle = pi * user_radius ** 2
print(user_area_of_circle)

# Get user input for personal information
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")

print(user_first_name, user_last_name, user_country, user_age)

# Check for Python reserved words
help('keywords')



