#power function, a to the power of b
def power_nums(a, b):
    try:
        return a ** b
    except:
        print("Error! The values are not numbers.")

#root function,root a (positive number)
def root(a):
    try:
        if a < 0:
            print("Enter a positive number")
            return
        return a ** 0.5
    except:
        print("Error! The input is not a number.")
# absolut value function, abs a
def absolut_value(a):
    try:
        if a < 0:
            return a * -1
        return a
    except:
        print("Error! The input is not a number.")