print("If user Enter 1 - Addition\n If user Enter 2 - Subtraction\n If user Enter 3 - Division\n If user Enter 4 - Multiplication\n If user Enter 5 - Addition")
inputNum = int(input("Enter the number: "))
if inputNum == 1:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = num1 + num2
elif inputNum == 2:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = num1 - num2

elif inputNum == 3:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = num1 / num2

elif inputNum == 4:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = num1 * num2

else:
    first = int(input("Enter the first number to calculate the average: "))
    second = int(input("Enter the second number to calculate the average: "))
    result = (first + second)/2

if result < 1:
    print("NEGATIVE")
