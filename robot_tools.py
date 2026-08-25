from calculator import Calculator


class RobotTools:

    def __init__(self):

        self.calculator = Calculator()


    def use_calculator(self, operation, a, b):

        if operation == "add":

            return self.calculator.add(a, b)


        elif operation == "subtract":

            return self.calculator.subtract(a, b)


        elif operation == "multiply":

            return self.calculator.multiply(a, b)


        elif operation == "divide":

            return self.calculator.divide(a, b)


        return "Operation not found."
