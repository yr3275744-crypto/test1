# add function add b to a
def add(a,b):
    try:
        return a+b
    except:
        print("the values are not numbers")
# sub function sub b to a
def subtract(a,b):
    try:
        return a - b
    except:
        print("the values are not numbers")

# multiplay fun multiplay b to a
def multiply(a,b):
    try:
        return a*b
    except:
        print("the values are not numbers")

# divide function divide a to b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("you cannot divide by zero")

    except TypeError:
        print("the values are not numbers")


