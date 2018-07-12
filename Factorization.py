'''
Factorization is the process of decomposition into prime factors. More precisely, for a given
number x we want to find primes p1, p2,...,pk whose product equals x.
Use of the sieve enables fast factorization. Let’s modify the sieve algorithm slightly. For
every crossed number we will remember the smallest prime that divides this number.
'''


# Preparing the array F for factorization
def arrayF(n):
    F = [0] * (n + 1)
    i=2
    while (i * i <= n):
        if (F[i] == 0):
            k=i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i
                k += i
        i += 1
    return F


# Factorization of x — O(log x)
def factorization(x, F):
    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x //= F[x]
    primeFactors += [x]
    return primeFactors


print(arrayF(20))
F = arrayF(20)
print(factorization(16, F))