
def modulo3(n):
    if n % 3: return False
    else: return True

def modulo5(n):
    if n % 5: return False
    else: return True

def sumOfEvenNumbers(list):
    sumOfEvenNumbers = 0
    for n in list:
        if not n % 2:
            sumOfEvenNumbers = sumOfEvenNumbers + n
    return sumOfEvenNumbers

def fibonacci(highestFibonacciNumber):
    i = 1
    j = 2
    fibNumbers = [i]
    while j < highestFibonacciNumber:
        fibNumbers.append(j)
        k = i + j
        i = j
        j = k
    return fibNumbers

def factorize(n):
    reminder = n
    factors = []
    i = 2
    while reminder > 1:
        if not reminder % i:
            factors.append(i)
            reminder = reminder / i
            i = i - 1
        i = i + 1
    return factors
