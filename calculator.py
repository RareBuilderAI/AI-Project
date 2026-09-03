class Calculator:

    def add(self, a, b):
        return a + b


    def subtract(self, a, b):
        return a - b


    def multiply(self, a, b):
        return a * b


    def divide(self, a, b):

        if b == 0:
            return "Cannot divide by zero"

        return a / b


    def calculate(self, command):

        command = command.lower().strip()

        parts = command.replace(",", " ").split()

        if len(parts) < 3:
            return (
                "🧮 Calculator\n"
                "Use: calculate 10 + 5"
            )

        try:

            first_number = float(parts[1])
            operator = parts[2]
            second_number = float(parts[3])

        except (ValueError, IndexError):

            return (
                "🧮 Calculator\n"
                "Use: calculate 10 + 5"
            )

        if operator == "+":

            result = self.add(
                first_number,
                second_number
            )

        elif operator == "-":

            result = self.subtract(
                first_number,
                second_number
            )

        elif operator == "*":

            result = self.multiply(
                first_number,
                second_number
            )

        elif operator == "/":

            result = self.divide(
                first_number,
                second_number
            )

        else:

            return (
                "🧮 Invalid operation.\n"
                "Use +, -, *, or /."
            )

        return f"🧮 Result: {result}"


def run_calculator():

    calculator = Calculator()

    print("🧮 Calculator")
    print("Type 'quit' to exit.")

    while True:

        operation = input(
            "\nChoose an operation (+, -, *, /): "
        )

        if operation.lower() == "quit":

            print("Calculator closed.")
            break

        if operation not in ["+", "-", "*", "/"]:

            print("Invalid operation.")
            continue

        try:

            first_number = float(
                input("Enter first number: ")
            )

            second_number = float(
                input("Enter second number: ")
            )

        except ValueError:

            print("Please enter valid numbers.")
            continue

        if operation == "+":

            result = calculator.add(
                first_number,
                second_number
            )

        elif operation == "-":

            result = calculator.subtract(
                first_number,
                second_number
            )

        elif operation == "*":

            result = calculator.multiply(
                first_number,
                second_number
            )

        else:

            result = calculator.divide(
                first_number,
                second_number
            )

        print("Result:", result)
