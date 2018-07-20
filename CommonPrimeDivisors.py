'''
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Assume that:

Z is an integer within the range [1..6,000];
each element of arrays A, B is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(Z*log(max(A)+max(B))2);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
'''


def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)


def hasSameFactors(p, q):
    if p == q == 0:
        return True

    denom = gcd(p, q)

    while (p != 1):
        p_gcd = gcd(p, denom)
        if p_gcd == 1:
            break
        p /= p_gcd
    else:
        while (q != 1):
            q_gcd = gcd(q, denom)
            if q_gcd == 1:
                break
            q /= q_gcd
        else:
            return True

    return False


def solution(A, B):
    # write your code in Python 3.6
    n = len(A)
    counter = 0
    for i in range(n):
        if hasSameFactors(A[i], B[i]):
            counter += 1
    return counter

print(solution([15, 10, 9], [75, 30, 5]))