def temperature(c):
    k = (5/9) * (c - 32)
    return k

c = int(input())
print(temperature(c))