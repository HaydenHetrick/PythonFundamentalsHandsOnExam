# Task 1: Data Types

age = 17
temperature = 59
too_hot = temperature > 70.0
too_cold = temperature < 60.00

print(age)
print(temperature)
print(too_hot)
print(too_cold) 

addition = age + temperature
subtraction = age - temperature
multiplication = age * temperature
division = age / temperature
square = age ** 2

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Square: {square}")

intro = "Hello World"
print("intro")

first_name = input("Please Enter Your First name: ")
print(first_name)

# Task 2: Functions

def calculate_area(Length, Width):
    area = length * width
    return area

length = 5.0 
width = 3.0
area = calculate_area(length, width)
print(f"The Rectangles Area is: {area}")

# Task 3: Logic Control

def check_number(number):
    if number > 0:
        print(f"{number} is positive ")
    elif number < 0:
        print(f"{number} is negative ")
    else:
        print(f"{number} is zero ")

check_number(5)
check_number(-2)
check_number(0)

# Task 4: Loops

