import math

def do_math(operator):
    if operator == "6":
        val1 = float(input("\nEnter value for extracting the square root: "))
        final = math.sqrt(val1)
    elif operator == "7":
        val1 = float(input("\nEnter value for calculating the logarithm to base 2: "))
        final = math.log(val1, 2)
    else:
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        if operator == "0":
            final = val1 + val2
        elif operator == "1":
            final = val1 - val2
        elif operator == "2":
            final = val1 * val2
        elif operator == "3":
            final = val1 / val2
        elif operator == "4":
            final = val1 % val2
        elif operator == "5":
            final = math.pow(val1, val2)

    return "\nThe result is: " + str(final) + "\n"

def back_to_menu():
    back = input("\nGo back to the main menu? (y/n) ")

    if back == 'y':
        return True
    elif back == 'n':
        return False

while True: 
    print("\nChoose the math operation. \n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")

    oper = input("\nYour option from the menu: ")

    print(do_math(oper))

    if back_to_menu():
        continue
    else:
        break

