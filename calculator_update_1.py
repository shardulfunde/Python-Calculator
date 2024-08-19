#taking Input
while True:
    a = int(input("What Are We doing Today?\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division?\n"))
    if a > 4 or a < 1:
        print("Please Select a valid number form 1 to 4")
        continue
    else:
        break
    
    
   
#Taking x and y
x = float(input("What's X?"))
y = float(input("What's Y?"))


#defining operators
def addition():
    print(x," + ",y," is",x + y)

def subtraction():
    print(x," - ",y," is ",x - y)

def multiplication():
    print(x," * ",y," is ",x * y)

def division():
    print(x," / ",y," is ",x / y)


    
#Adding if statements to react on input
if a == 1:
    addition()

elif a == 2:
    subtraction()

elif a == 3:
    multiplication()

else:
    division()

