#                            Assignment - 1

"""
Q1. Create variables of different data types (string, integer, float, Boolean)
and print their values and types.
"""

string = "Atharva"
num = 5
float_var = 3.141592653596
boolean = True

print(string,type(string))
print(num, type(num))
print(float_var, type(float_var))
print(boolean, type(boolean))

"""
Q2. Write a Python program that asks the user for their name and age,
then prints a message saying "Hello, [Name]! You are [Age] years old."
"""

def hello_user():
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    print("Hello,", name, "! You are", age, "years old.")
hello_user()

"""
Q3. 3.	Create a simple calculator that allows the user to input two numbers
and an operator (+, -, *, /, %, **, //). Based on the operator provided,
the program should perform the corresponding arithmetic operation and display
the result.
"""

def calculator():
    print(eval(input("Enter an expression to calculate : ")))
calculator()

"""
Q4. Write a Python program that takes the length and width of a rectangle
as input and calculates its area and perimeter. Display the results.
"""

def area_perimeter():
    length = float(input("Enter length = "))
    breadth = float(input("Enter breadth = "))
    area = length * breadth
    perimeter = 2 * (length + breadth)
    print(f"Area = {area}\nPerimeter = {perimeter}")

area_perimeter()

"""
Q5. 5.	Write a Python program that takes an integer as input 
and determines if it is even or odd. Print the result.
"""

def even_odd():
    a = int(input("Enter an integer : "))
    print(f"{a} is {'even' if a%2 == 0 else 'odd'}")

even_odd()

"""
Q6. Write a Python program that takes the principal amount, rate of interest,
and time period as inputs and calculates the simple interest.
Display the calculated interest.
"""

def simple_interest():
    p = float(input("Enter principal amount = "))
    r = float(input("Enter Rate of interest = "))
    n = float(input("Enter time in years = "))

    simple_interest_amount = (p * r * n) / 100
    print(f"Simple Interest = {simple_interest_amount}")

simple_interest()

"""
Q7. Write a Python program that takes three numbers as input and calculates their
average. Print the result.
"""

def avg():
    a, b, c = map(float,(input("Enter 3 numbers with space : ").split()))
    print(f"Average = ", (a+b+c)/3)

avg()

"""
Q8. Write a Python program that converts temperature from Celsius to
Fahrenheit and vice versa. The program should ask the user for the temperature
value and the unit (Celsius or Fahrenheit) and then perform the conversion.
"""

def temp_converter():
    while True:
        convert = input("Choose an option:\n" \
        "1) Celsius to Fahr\n" \
        "2) Fahr to Celsius\n" \
        "3)exit\n" \
        "\n===> "
        )
        match convert:
            case '1':
                celsius = float(input("Enter temperature in Celsius: "))
                fahr = (celsius * 9 / 5) + 32
                print(f"{celsius}°C = {fahr}°F")

            case '2':
                fahr = float(input("Enter temperature in Fahrenheit: "))
                celsius = (fahr - 32) * 5 / 9
                print(f"{fahr}°F = {celsius}°C")

            case '3':
                return

            case _:
                print("Error.....Invalid entry.")

temp_converter()

"""
Q9. Write a Python program that calculates the Body Mass Index (BMI) based
on user input for weight (in kg) and height (in meters). The formula for BMI
is weight / (height ** 2). Display the BMI and categorize it as underweight,
normal weight, overweight, or obese.
"""

def calculate_bmi():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)
    print(f"Your BMI is {bmi:.1f}")

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You have a normal weight.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

calculate_bmi()

"""
Q10. Write a Python program that takes two numbers as input and compares them.
Print whether the first number is greater than, less than, or equal to the second
number.
"""

def compare_numbers():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    if first_number > second_number:
        print("The first number is greater.")
    elif first_number < second_number:
        print("The first number is less.")
    else:
        print("The numbers are equal.")

compare_numbers()