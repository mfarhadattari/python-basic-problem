def fibonacci(num):
    fibo = [0, 1]
    i = 2
    while(i <= num):
        nextFibo = fibo[i-1] + fibo[i-2]
        fibo.append(nextFibo)
        i+=1
    return fibo

print(fibonacci(10))