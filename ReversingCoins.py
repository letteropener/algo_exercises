'''
Consider n coins aligned in a row. Each coin is showing heads at the beginning
[1,2,3,4,5,6,7,8,9,10]
Then, n people turn over corresponding coins as follows. Person i reverses coins with numbers
that are multiples of i. That is, person i flips coins i, 2i, 3i, . . . until no more appropriate
coins remain. The goal is to count the number of coins showing tails. In the above example,
the final configuration is:
[2,3,5,6,7,8,10]

Tails: 1,4,9
'''

# O(n log n):
'''
The number of operation can be estimated by n/1 +n/2 +. . .+n/n, what equals 
n·(1/1 + 1/2 +. . .+ 1/n).
The sums of multiplicative inverses (reciprocals) of the first n numbers are 
called harmonic numbers, which asymptotically equal O(log n). In summary, 
the total time complexity is O(n log n).
'''
def coins(n):
    result = 0
    coin = [0] * (n + 1)
    for i in range(1, n + 1):
        k = i
        while (k <= n):
            coin[k] = (coin[k] + 1) % 2
            k += i
        result += coin[i]
    return result

print(coins(10))