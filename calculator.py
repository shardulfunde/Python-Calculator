def main():
    print("What are we gonna do today?")
    print("1)Addition")
    print("2)Substraction")
    print("3)Multiplication")
    print("4)Division")
    a = int(input(" "))
    
    x = float(input("What's X?"))
    y = float(input("What's Y?"))

    def addition():
        z = round(x + y, 2)
        print(x,"+",y,"is",z)

    def substraction():
        z = round(x - y, 2)
        print(x,"-",y,"is",z)

    def multiplication():
        z = round(x * y, 2)
        print(x,"x",y,"is",z)

    def division():
        z = round(x / y, 2)
        print(x,"/",y,"is",z)

    if a == 1:
        addition()

    elif a == 2:
        substraction()

    elif a == 3:
        multiplication()

    elif a == 4:
        division()

    else:
        print("Bro,are you high are what?")

main()



  
