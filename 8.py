inputString = input("Enter the string: ")
a =0
n =0
for i in inputString:
    if i.isalpha():
        a+=1
    else:
        n+=1    
print("Letters ",a)
print("Digits ", n)