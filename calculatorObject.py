class Calculator:

    # private variables
    num1 = 0
    num2 = 0
    first = True

    # public variables
    def __init__(self):
        self.sign = "+"
        self.loop = True

    #setters
    def set_sign(self):
        if self.first:
            print("Hi this is a calculator\nEnter + - * / to choose what type of math you would like:")
            self.sign = str(input())
        else:
            print("Enter + - * / to choose what type of math you would like:")
            self.sign = str(input())
    def set_nums(self):
        print("What numbers would you like to enter, separate the numbers with a new line:")
        self.num1 = float(input())
        self.num2 = float(input())
    def another(self):
        print("Would you like to do more math? y,n")
        loop = input()
        if loop.lower() == "y":
            self.loop = True
        else:
            self.loop = False

    #getters (unused)
    def get_loop(self):
        return self.loop
    def get_sign(self):
        return self.sign

    # math
    def add(self):
        result = str(self.num1 + self.num2)
        print("Result: " + result + "\n")
        self.another()
        self.first = False
    def sub(self):
        result = str(self.num1 - self.num2)
        print("Result: " + result + "\n")
        self.another()
        self.first = False
    def mult(self):
        result = str(self.num1 * self.num2)
        print("Result: " + result + "\n")
        self.another()
        self.first = False
    def divide(self):
        result = str(self.num1 / self.num2)
        print("Result: " + result + "\n")
        self.another()
        self.first = False
    def wrong(self):
        print("Not a valid sign, please try again:\n")
        self.first = False

#define the class
calc = Calculator()
#loop through calculator
while calc.loop:
    calc.set_sign()
    calc.set_nums()
    if calc.sign == "+":
        calc.add()
    elif calc.sign == "-":
        calc.sub()
    elif calc.sign == "*":
        calc.mult()
    elif calc.sign == "/":
        calc.divide()
    else:
        calc.wrong()