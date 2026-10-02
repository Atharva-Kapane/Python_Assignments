#                       Assignment 4

"""
Q1. Create a Python module with a function that calculates the area of
a circle. Import this module in another script and use it to find the area 
for a radius of 5.
"""

# %%
from custom.assign_4_area_of_circle import area_of_circle
area_of_circle(5)


# %%
"""
Q2. Create a function that imports date time and returns the current date
and time.
Example: current_datetime() should return the current timestamp like
"2023-09-14 15:30:25"
"""

def curr_datetime():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

curr_datetime()


# %%
"""
Q3. Create a lambda function to check if a string starts with the letter 'A'.
Example: (lambda s: s[0]. lower() == 'a')('Apple') should return True.
"""

startswith_A = lambda string: string[0].lower() == 'a'
startswith_A("Atharva")
startswith_A("alpha")
startswith_A("romeo")

# startswith_A = lambda string: string.startswith('A')
# startswith_A("Atharva")

# %%
"""
Q4. Write a function that imports your custom module (e.g., math_utils.py)
and uses a function from it to calculate the factorial of a number.
"""

from custom.assign_4_factorial import factorial
factorial(7)


# %%
"""
Q5. Create a function that rounds a list of numbers to the nearest whole number.
Example: round_list([1.2, 2.5, 3.8]) should return [1, 3, 4].
"""

def round_list():


# %%
Use round() inside map() to round a list of floating-point numbers to 1 decimal place. Example: round_to_one([3.14159, 2.71828, 1.61803]) should return [3.1, 2.7, 1.6].





Write a function that takes two lists and uses map() to return a list of the sums of corresponding elements.

Example: add_lists([1, 2], [3, 4]) should return [4, 6].
# %%
