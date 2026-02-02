def return_quare_area(side):
    try:
        if side < 0:
            print("Negative side length is not possible.")
            return
        return side * side
    except:
        print("the value is not a number")
def return_rectangular_area(side_a, side_b):
    try:
        if side_a < 0 or side_b < 0:
            print("Negative side length is not possible.")
            return
        return side_a * side_b
    except:
        print("there have a value that is not a number")