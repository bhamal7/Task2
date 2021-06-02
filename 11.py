counter = 1
guessNum = 3
while counter <= 5:
    print("Type in the ",counter, "number: ")
    inputNum = int(input())
    counter +=1
    if inputNum == guessNum:
        print("Good guess!")
        break
    print("Try again!")
   
print("Sorry but that was not very successful")