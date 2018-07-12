'''
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Assume that:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P, Q is an integer within the range [1..N];
P[i] ≤ Q[i].
Complexity:

expected worst-case time complexity is O(N*log(log(N))+M);
expected worst-case space complexity is O(N+M) (not counting the storage required for input arguments).
'''

def solution(N, P, Q):
    # write your code in Python 3.6
    prime_list = [0]*(1 + N)
    i = 2
    while(i*i <= N):
        if prime_list[i] == 0:
            k = i*i
            while (k <= N):
                if prime_list[k] == 0:
                    prime_list[k] = i
                k += i
        i += 1
    subprime_prefixsum = [0]*(1 + N)
    for i in range(4,N+1):
        if prime_list[i] != 0 and prime_list[i // prime_list[i]] == 0:
            subprime_prefixsum[i] = subprime_prefixsum[i-1]+1
        else:
            subprime_prefixsum[i] = subprime_prefixsum[i - 1]
    len_P = len(P)
    output_list = []
    for i in range(len_P):
        output_list.append(subprime_prefixsum[Q[i]] - subprime_prefixsum[P[i]-1])
    return output_list

print(solution(26,[1,4,26],[26,10,26]))