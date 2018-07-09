'''
The leader of this sequence is the element whose
value occurs more than n/2 times

The leader may be found in many ways. We describe some methods here, starting with
trivial, slow ideas and ending with very creative, fast algorithms. The task is to find the value
of the leader of the sequence a0, a1,...,an-1, such that 0 <= ai <= 10^9. If there is no leader,
the result should be -1.
O(n)time complexity
'''

def goldenLeader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if (A[k] == candidate):
            count += 1
        if (count > n // 2):
            leader = candidate
    return leader

print(goldenLeader([4,6,6,6,6,8,8]))
