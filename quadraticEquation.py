def rootOfQuadraticEquation(a,b,c):
    D = (b*b)-(4*a*c)
    if(D > 0):
        root1 = (-b + (D ** 1/2)) / (2*a)
        root2 = (-b - (D ** 1/2)) / (2*a)
        return [root1, root2]
    elif(D == 0):
        root = -b / (2*a)
        return root
    else:
        return "Complex Root"
    
print(rootOfQuadraticEquation(1, -2, -15))