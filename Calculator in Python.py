import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by ZERO")
    return x / y

def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))

def cosecant(angle):
    return 1 / math.sin(math.radians(angle))

def secant(angle):
    return 1 / math.cos(math.radians(angle))

def cotangent(angle):
    return math.cos(math.radians(angle)) / math.sin(math.radians(angle))

def calculator():
    print("Welcome to the Calculator!")
    print("Available operations: \n+ (addition) \n- (subtraction) \n* (multiplication) \n/ (division)")
    print("sin (sine) \ncos (cosine) \ntan (tangent) \ncosec (cosecant) \nsec (secant) \ncot (cotangent)")

    while True:
        try:
            operation = input("Enter the operation you want to perform: ")
            if operation in ['+', '-', '*', '/']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if operation == '+':
                    result = add(num1, num2)
                elif operation == '-':
                    result = subtract(num1, num2)
                elif operation == '*':
                    result = multiply(num1, num2)
                elif operation == '/':
                    result = divide(num1, num2)

            elif operation in ['sin', 'cos', 'tan', 'cosec', 'secant', 'cot']:
                angle = float(input("Enter the angle in degrees: "))

                if operation == 'sin':
                    result = sine(angle)
                elif operation == 'cos':
                    result = cosine(angle)
                elif operation == 'tan':
                    result = tangent(angle)
                elif operation == 'cosec':
                    result = cosecant(angle)
                elif operation == 'sec':
                    result = secant(angle) 
                elif operation == 'cot':
                    result = cotangent(angle)

            else:
                print("Invalid operation. Please try again.")
                continue

            print("Result:", result)

        except ValueError as e:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print("Error:", str(e))

        again = input("Do you want to perform another calculation? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    calculator()