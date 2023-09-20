# PYTHON BASIC PROBLEM

- Is Leap Year
- Word Count in string
- Count number of vowels
- Remove Duplicate from list
- Fibonacci Seres
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
