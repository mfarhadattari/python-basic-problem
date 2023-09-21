num1 = float(input("Number1: "))
operator = input("Operator: ")
num2 = float(input("Number2: "))

if(operator == "+"):
    print("Result: ", num1 + num2)
elif(operator == "-"):
    print("Result: ", num1 - num2)
elif(operator == "*"):
    print("Result: ", num1 * num2)
elif(operator == "/"):
    print("Result: ", num1 / num2)
else:
    print("Something went wrong!")
    
    