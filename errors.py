# This example program is meant to demonstrate errors.

print("Welcome to the error program")  # Fixed Syntax Error: Added parentheses for print function

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"  # Fixed Syntax Error: Changed '==' to '=' and Logical Error: Removed non-numeric characters
age = int(age_Str)  # Fixed Runtime Error: Correct type conversion
print("I'm " + str(age) + " years old.")  # Fixed Syntax Error: Concatenated strings correctly

# Variables declaring additional years and printing the total years of age
years_from_now = 3  # Fixed Logical Error: Changed to integer for calculation
total_years = age + years_from_now  # Fixed Logical Error: Correctly calculated total years

print("The total number of years: " + str(total_years))  # Fixed Syntax Error: Correct string concatenation

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12  # Fixed Logical Error: Correctly calculated total months
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")  # Fixed Syntax Error: Correct string concatenation

# HINT, 330 months is the correct answer
