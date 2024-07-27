def addition():
    a = float(input("Enter first value "))
    b = float(input("Enter second value "))
    print("Your answer is ", a+b)

def subtraction():
    a = float(input("Enter first value "))
    b = float(input("Enter second value "))
    print("Your answer is ", a-b)

def multiplication():
    a = float(input("Enter first value "))
    b = float(input("Enter second value "))
    print("Your answer is ", a*b)

def division():
    a = float(input("Enter first value "))
    b = float(input("Enter second value "))
    print("Your answer is ", a/b)


while 1:
    print("Welcome to the basic calculator made by Keyaan")
    print("what arithmetic operation do you want to do?")
    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. quit")
    print("type respective numbers")
    operation = int(input())

    if operation == 4:
        print("Division Operation selected")
        division()
    elif operation == 1:
        print("Addition Operation selected")
        addition()
    elif operation == 2:
        print("Subtraction Operation selected")
        subtraction()
    elif operation == 3:
        print("Multiplication Operation selected")
        multiplication()
    elif operation == 5:
        break
    else:
        print("enter a valid value")
        
      
