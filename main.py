from helper_functions import *

should_loop_continue = True

while should_loop_continue:
    first_number = input_number("first")
    continue_with_old_answer = ""
    while continue_with_old_answer != "n":
        operation_choice = input_operation_choice()
        if operation_choice == "0":
            print("\nGoodbye!")
            exit()
        second_number = input_number("second")
        if operation_choice == "/" and second_number == 0:
            print(f"{stars_line}\n"
                  f"ERROR: Division by Zero"
                  f"{stars_line}")
        else:
            answer = perform_operation(first_number, second_number, operation_choice)
            continue_with_old_answer = continue_calculation_choice(answer)
            if continue_with_old_answer == "exit":
                print("\nGoodbye!")
                exit()
            elif continue_with_old_answer == "y":
                first_number = answer
            elif continue_with_old_answer != "n":
                print(f"{stars_line}"
                      f"\nKindly enter a valid value!"
                      f"{stars_line}")
    else:
        clear_screen()
