def countVowel(word):
    vowels = 'aeiou'
    numOfVowel = 0
    for i in word:
        for c in vowels:
            if i == c:
                numOfVowel += 1
    return numOfVowel
        
print(countVowel("hello"))