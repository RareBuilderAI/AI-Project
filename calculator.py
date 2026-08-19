def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose operation (1-4): ")

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))


if choice == "1":
    print("Result:", add(number1, number2))

elif choice == "2":
    print("Result:", subtract(number1, number2))

elif choice == "3":
    print("Result:", multiply(number1, number2))

elif choice == "4":
    print("Result:", divide(number1, number2))

else:
    print("Invalid choice")