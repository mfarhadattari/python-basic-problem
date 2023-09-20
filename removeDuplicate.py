def removeDuplicate(array):
    uniqueArray = []
    for i in array:
        if i not in uniqueArray:
            uniqueArray.append(i)

    return uniqueArray

numbers = [1, 2, 1, 3, 2, 5, 8, 5, 7]
print(removeDuplicate(numbers))