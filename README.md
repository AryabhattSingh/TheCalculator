# TheCalculator

## Overview

This console-based calculator program allows users to perform basic mathematical operations, including addition, subtraction, multiplication, and division. The program 
also features an ASCII art representation of a calculator for a user-friendly interface.

## Usage

1. **Program Start**: When you run the program, it will display an ASCII art representation of a calculator and prompt you to enter the first number.

2. **Input Validation**: Your input will be checked to ensure it's a valid number. If the input is invalid, a messgae will be displayed.

3. **Select Operation**: You will then be prompted to choose one of the following operations:
   - `EXIT`: To exit the program.
   - `+`: To perform addition.
   - `-`: To perform subtraction.
   - `*`: To perform multiplication.
   - `/`: To perform division.

4. **Operation Validation**: Your operation choice will be validated to ensure it's one of the valid options mentioned above.

5. **Performing Mathematical Operation**:
   - If you choose `EXIT`, the program will terminate, bidding you farewell with a "Goodbye!" message.
   - If you choose one of the four mathematical operations (+, -, *, /):
     - You will be prompted to enter the second number.
     - Your input will be checked to ensure it's a valid number.
     - The program will perform the selected mathematical operation using the first and second numbers.
     - The result will be displayed to you.

6. **Continuation Options**: After the calculation, you will have the following choices:
   - `EXIT`: To exit the program with a "Goodbye!" message.
   - `CONTINUE`: To continue with the current result. You will be prompted to choose another operation, and the process repeats.
   - `NEW`: To start a new calculation. The console will be cleared, and the program begins anew with the ASCII art calculator.

## Running the Program

To run the program, follow these steps:
1. Make sure you have a compatible Python interpreter installed on your system.
2. Download the program's source code.
3. Open your terminal or command prompt.
4. Navigate to the directory where the program's source code is located.
5. Run the program by executing the Python script.

Example:
```shell
python main.py
```

## License

This program is released under the MIT License. You are free to use, modify, and distribute it as per the terms of the license. Please refer to the [LICENSE](LICENSE) 
file for details.

Feel free to reach out if you have any questions or need further assistance. Enjoy using the console-based calculator program!
