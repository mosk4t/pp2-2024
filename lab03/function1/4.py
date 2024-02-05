def isPrime(a):
    if a<2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

nums = input().split()
prime_list = []
for i in nums():
	if isPrime(int(i)):
		prime_list.append(i)
print(prime_list)