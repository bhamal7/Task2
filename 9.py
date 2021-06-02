

guessNum = 3
while True:

    inputNum = int(input("Entert the guess number: "))
    if inputNum == guessNum:
        break
    else:
        inputQ = input("Do you want to guess again: ")
        if inputQ == "yes":
            inputNum2 = int(input("Entert the guess number: "))
            if inputNum2 == guessNum or inputQ == "no":
                break
        else:
            break    
