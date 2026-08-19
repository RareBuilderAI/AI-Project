from datetime import datetime


class Tools:
    def get_date(self):
        return str(datetime.now().date())

    def calculate(self, expression):
        return str(eval(expression))