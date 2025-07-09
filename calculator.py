
def get_nums():
    print("What numbers would you like to enter, separate the numbers with a new line:")
    num1 = float(input())
    num2 = float(input())
    return num1, num2

def another():
    print("Would you like to do more math? y,n")
    loop = input()
    if loop.lower() == "y":
        return True
    else:
        return False
    
def get_sign(first):
    if first:
        print("Hi this is a calculator\nEnter + - * / to choose what type of math you would like:")
        return input()
    else:
        print("Enter + - * / to choose what type of math you would like:")
        return input()


loop = True
first = True

while loop:
    sign = str(get_sign(first))
    if sign == "+":
        num1, num2 = get_nums()
        result = num1 + num2
        result = str(result)
        print("Result: " + result + "\n")
        loop = another()
    elif sign == "-":
        num1, num2 = get_nums()
        result = num1 - num2
        result = str(result)
        print("Result: " + result + "\n")
        loop = another()
    elif sign == "*":
        num1, num2 = get_nums()
        result = num1 * num2
        result = str(result)
        print("Result: " + result + "\n")
        loop = another()
    elif sign == "/":
        num1, num2 = get_nums()
        result = num1 / num2
        result = str(result)
        print("Result: " + result + "\n")
        loop = another()
    else:
        print("Not a valid sign, please try again:\n")
    first = False
    