#
#  Overview
#
# In this project, you will build a scientific calculator on the command line. The program will display a menu of options which includes several arithmetic operations as well as options to display statistics and exit the program. The project is designed to give you an opportunity to practice looping, type conversion, and data persistence.
#
# Submission Instructions
#
# After completing all programs, please submit your .py files labeled with the lab number.
#
# For example: Lab3.py
#
# You have Unlimited Submissions before the deadline!!
#
#  Specification
#
# When the program starts it should display a menu, prompt the user to enter a menu option, and read values:
#
# Current Result: 0.0
#
# Calculator Menu
# ---------------
# 0. Exit Program
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exponentiation
# 6. Logarithm
# 7. Display Average
#
# Enter Menu Selection: 1
#
# When an option with operands (1-6) is selected, the program should prompt for and read floating point numbers as follows:
#
# Enter first operand: 89.1
# Enter second operand: 42
#
#
# Once the two operands have been read, the result should be calculated and displayed, along with the menu:
#
# Current Result: 131.1
#
# Calculator Menu
# ---------------
# ...
#
# Operational Behavior
#
# This calculator includes multiple behaviors that are unique depending on the input and operation specified; they are detailed in this section. Use Python's “math” library.
#
# Exponentiation
# For exponentiation, the second operand should be used as the base and the first as the exponent   i.e.: If the second operand is 2 and the second is 4:  24=16.
#
# Logarithm
# For exponentiation, the first operand should be used as the base and the second as the exponent   i.e.: If the first operand is 2 and the second is 4: log24 = 2.
#
# Displaying the Average
# As the program progresses, it should store the total of all results of calculation and the number of calculations. Not that this does NOT include the starting value of 0. The program should display the average of all calculations as such:
#
# Sum of calculations: 101.3
# Number of calculations: 2
# Average of calculations: 50.15
#
# Note that the average calculation should show a maximum of two decimal places. The program should immediately prompt the user for the next menu option (without redisplaying the menu).
#
# If no calculations have been performed, this message should be displayed:
#
# Error: No calculations yet to average!
#
#
#
# Assumptions and Notes
#
# If the menu option is invalid, output: "Invalid selection." without displaying the menu again. This menu option will be an integer, but not necessarily valid.
# If the operands are invalid (i.e., not applicable for certain operations – see below), output: “Error: invalid input!” without displaying the menu again (no operation is completed).
# If the operand is RESULT, use the result of the previous calculation for that operand.
#
# Certain operations have limitations on their inputs (such as division: a/b, b != 0), so ensure that this is accounted for in your program.
#
# Sample Submission Output
#
# Example:
#
# Current Result: 0.0
#
# Calculator Menu
# ---------------
# 0. Exit Program
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exponentiation
# 6. Logarithm
# 7. Display Average
#
# Enter Menu Selection: 7
# Error: No calculations yet to average!
#
# Enter Menu Selection: 1
# Enter first operand: 0.5
# Enter second operand: -2.5
# Current Result: -2.0
#
# Calculator Menu
# ---------------
# 0. Exit Program
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exponentiation
# 6. Logarithm
# 7. Display Average
#
# Enter Menu Selection: 5
# Enter first operand: -2.0
# Enter second operand: -2.0
# Current Result: 0.25
#
# Calculator Menu
# ---------------
# 0. Exit Program
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exponentiation
# 6. Logarithm
# 7. Display Average
#
# Enter Menu Selection: 6
# Enter first operand: 2
# Enter second operand: 0.5
# Current Result: -1.0
#
# Calculator Menu
# ---------------
# 0. Exit Program
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exponentiation
# 6. Logarithm
# 7. Display Average
#
# Enter Menu Selection: 7
# Sum of calculations: -2.75
# Number of calculations: 3
# Average of calculations: -0.92
#
# Enter Menu Selection: -10
# Error: Invalid selection!
#
# Enter Menu Selection: 0
# Thanks for using this calculator. Goodbye!
import math

def scientificcalculator():
    isRunning = True
    result = 0.0
    calculations = 0
    menuSelection = 1
    sumOfCalculations = 0
    while isRunning:
        if (menuSelection == 1 or menuSelection == 2 or menuSelection == 3 or menuSelection == 4 or menuSelection == 5 or menuSelection == 6):
            print(f'Current Result: {result}\n\nCalculator Menu\n---------------\n0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average\n')
        menuSelection = int(input('Enter Menu Selection: '))
        if menuSelection == 1 or menuSelection == 2 or menuSelection == 3 or menuSelection == 4 or menuSelection == 5 or menuSelection == 6:
            firstOperand = float(input('Enter first operand: '))
            secondOperand = float(input('Enter second operand: '))
            if menuSelection == 1:
                result = firstOperand+secondOperand
            if menuSelection == 2:
                result = firstOperand-secondOperand
            if menuSelection == 3:
                result = firstOperand*secondOperand
            if menuSelection == 4 and secondOperand != 0:
                result = firstOperand/secondOperand
            if menuSelection == 5:
                result = firstOperand**secondOperand
            if menuSelection == 6 and secondOperand > 0 and firstOperand > 0:
                result = math.log(secondOperand,firstOperand)
            calculations += 1
            sumOfCalculations += result
        elif menuSelection == 7:
            if calculations != 0:
                print(f'Sum of calculations: {sumOfCalculations}\nNumber of calculations: {calculations}\nAverage of calculations: {round((sumOfCalculations/calculations),2)}\n')
            else:
                print('Error: No calculations yet to average!\n')
        elif menuSelection == 0:
            print('Thanks for using this calculator. Goodbye!')
            isRunning = False
        else:
            print('Error: Invalid selection!\n')
scientificcalculator()