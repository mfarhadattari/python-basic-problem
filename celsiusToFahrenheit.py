def celsiusToFahrenheit(temperature):
    result = (temperature * 9 / 5) + 32
    return result

def fahrenheitToCelsius(temperature):
    result = (temperature - 32) * 5/9
    return result

temperature = float(input("Enter temperature: "))
unite = input("Enter unite: ")

if(unite == "C"):
    F = celsiusToFahrenheit(temperature)
    print("F = ", F)
elif(unite == "F"):
    C = fahrenheitToCelsius(temperature)
    print("C = ", C)
else:
    print("Something is wrong!")