a = 10
b = 20
c = 30
avg = (a +b + c)/3
print("avg = ", avg)
if (avg > a and avg > b and avg > c):
    print("avg is higher than a, b, c")
else:
    if (avg > a and avg > b):
        print("avg is higher than a, b, c")
    elif (avg > a and avg > c):
        print("avg is higher than a, b, c")
    elif (avg > c and avg > b):
        print("avg is higher than a, b, c")
    elif (avg > a):
        print("avg is just higher than a")
    elif (avg > b):
        print("avg is just higher than b")
    else:
        print("avg is just higher than c")




