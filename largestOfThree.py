def largestOfThree(a,b,c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c

result = largestOfThree(12,16,9)
print(result)