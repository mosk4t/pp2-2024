def isPrime(a):
    if a<2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

nums = [int(el) for el in input().split()]
primeNumbers = list(filter(lambda x: isPrime(x), nums))
print(primeNumbers)