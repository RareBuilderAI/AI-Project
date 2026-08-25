from calculator import Calculator


calculator = Calculator()


assert calculator.add(2, 3) == 5
assert calculator.subtract(5, 3) == 2
assert calculator.multiply(2, 3) == 6
assert calculator.divide(6, 3) == 2


print("Calculator tests passed!")