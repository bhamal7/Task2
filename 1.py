inputNum = int(input("Enter a number: "))
if inputNum % 3 ==0 and inputNum % 5 != 0:
    print("Consultadd")
elif inputNum % 5 ==0 and inputNum % 3 != 0:
    print("Python Training")
elif inputNum % 3 == 0 and inputNum % 5 == 0:
    print("Consultadd - Python Training") 
else:
    print("Not divisible by 3 or 5")

