def isPositiveOrNegative(number):
    if(number > 0):
        return "POSITIVE"
    elif(number < 0):
        return "NEGATIVE"
    else:
        return "ZERO"

number = float(input("Number = "))
print(isPositiveOrNegative(number))