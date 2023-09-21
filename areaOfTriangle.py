def areaOfTriangle(base, height):
    result = 1/2 * base * height
    return result

base = int(input("Base: "))
height = int(input("Height: "))
result = areaOfTriangle(base, height)
print(result)