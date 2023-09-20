# PYTHON BASIC PROBLEM

- Is Leap Year
- Word Count in string
- Count number of vowels
- Remove Duplicate from list
- Fibonacci Series
- Multiplication table

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
