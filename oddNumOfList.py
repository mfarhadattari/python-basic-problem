def filterOddNumbers(numbers):
    oddNumbers = []
    for i in numbers:
        if(i % 2 != 0):
            oddNumbers.append(i)
    return oddNumbers

print(filterOddNumbers([1,2,3,4,5, 9, 11]))