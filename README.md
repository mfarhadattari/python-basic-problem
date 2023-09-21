# PYTHON BASIC PROBLEM

- Is Leap Year
- Word Count in string
- Count number of vowels
- Remove Duplicate from list
- Fibonacci Series
- Multiplication table
- Arithmetic Calculator
- Area Of Rectangular
- Area of circle
- Fahrenheit to celsius converter
- Largest of 3 number
- Is even or odd
- Is positive or negative number
- Area of triangle
- Discount calculator
- Grade pointing
- Roots of quadratic equation
- Find odd numbers from list
- Is prime number
- Sum of arithmetic series
- Factorial
- Min and Max of list
- Sum of list

## Leap Year -

```python
# leap year problem
year = int(input("Year: "))
if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print(year ,"is Leap Year")
else:
    print(year ,"is Not Leap Year")
```

## Word Count of string

```python
# Word count of a string
def countWord(word):
    return len(word)

print(countWord("Farhad"))
```

## Count number of vowels

```python
def countVowel(word):
    vowels = 'aeiou'
    numOfVowel = 0
    for i in word:
        for c in vowels:
            if i == c:
                numOfVowel += 1
    return numOfVowel

print(countVowel("hello"))
```

## Remove Duplicate from list

```python
def removeDuplicate(array):
    uniqueArray = []
    for i in array:
        if i not in uniqueArray:
            uniqueArray.append(i)

    return uniqueArray

numbers = [1, 2, 1, 3, 2, 5, 8, 5, 7]
print(removeDuplicate(numbers))
```

## Fibonacci Series

```python
def fibonacci(num):
    fibo = [0, 1]
    i = 2
    while(i <= num):
        nextFibo = fibo[i-1] + fibo[i-2]
        fibo.append(nextFibo)
        i+=1
    return fibo

print(fibonacci(10))
```

## Multiplication table

```python
def multiplicationTable(num):
    i = 1
    while(i <= 10):
        print(num,"x",i, "= ", num*i)
        i+=1

multiplicationTable(5)
```

## Arithmetic Calculator

```python
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


```

## Area Of Rectangular

```python
def areaOfRectangular(length, width):
    return length * width

result = areaOfRectangular(20, 15)
print(result)
```

## Area of circle

```python
def areaOfCircle(radius):
    PI = 3.1416
    return PI*radius*radius

result = areaOfCircle(10)
print(result)
```

## Fahrenheit to celsius converter

```python
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
```
