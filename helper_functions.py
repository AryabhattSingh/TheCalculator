from calculator_operations import *
import os

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

stars_line = f"\n{'*' * 45}"


def input_number(number_order):
    """To take number input. It also checks the validity of the inputted number"""
    number = 0
    number_valid = False
    while not number_valid:
        number = input(f"\nEnter {number_order} number:")
        number_valid = is_input_number_valid(number)
    number = float(number)
    return number


def is_input_number_valid(number):
    """Takes a string as parameter and returns True if it can be type-casted into a floating point
    number, else returns False"""
    try:
        float(number)
        return True
    except ValueError:
        print(f"{stars_line}\nERROR: Only Integers Are Allowed{stars_line}")
        return False


def input_operation_choice():
    """Returns the operation_choice as a string which the user wants to perform on the numbers"""
    operation_choice = ""
    operation_choice_valid = False
    while not operation_choice_valid:
        operation_choice = input("\nAvailable operations: \n0 for EXIT"
                                 "\n+ for Addition\n- for Subtraction\n* for Multiplication"
                                 "\n/ for Division\n"
                                 "\nEnter your operation choice: ")
        if operation_choice in ["0", "+", "-", "*", "/"]:
            operation_choice_valid = True
        else:
            print(f"{stars_line}"
                  f"\nKindly enter a valid operation"
                  f"{stars_line}")
    return operation_choice


def perform_operation(first_number, second_number, operation_choice):
    """Takes two float numbers and operation_choice as string for parameters. Performs the
    specified mathematical operation using first and second numbers as operands"""
    function_name = operations[operation_choice]
    answer = function_name(first_number, second_number)
    if second_number < 0:
        second_number = f"({second_number})"
    print(f"{stars_line}\n"
          f"{first_number} {operation_choice} {second_number} = {answer}"
          f"{stars_line}")
    return answer


def continue_calculation_choice(answer):
    """Returns 'exit' if user wants to exit calculator or, 'y' or 'n' based on whether the user
     wants to continue calculation with the result of the previous calculation"""
    choice = ""
    choice_valid = False
    while not choice_valid:
        choice = input(f"\nType 'exit' to EXIT or,"
                       f"\nType 'y' to continue calculating with {answer} or,"
                       f"\nType 'n' to start a new calculation:")
        if choice not in ["exit", "y", "n"]:
            print(f"{stars_line}\n"
                  "Kindly enter a valid value"
                  f"{stars_line}")
        else:
            choice_valid = True
    return choice


def clear_screen():
    os.system('cls')
