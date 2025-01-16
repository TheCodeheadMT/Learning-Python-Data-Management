
class Calculator:
    # Class variable
    operations = ["add", "subtract", "multiply", "divide"]

    def __init__(self, a, b):
        self.a = a  # Instance variable
        self.b = b  # Instance variable

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

if __name__ == "__main__":
    calc = Calculator(10, 5)
    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
