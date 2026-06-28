# Input and Output Function Errors

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("Name:", name)
    print("Age:", age)

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    print("Division =", a / b)

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except NameError:
    print("Error: Variable is not defined.")

except TypeError:
    print("Error: Invalid data type.")

except Exception as e:
    print("Error:", e)