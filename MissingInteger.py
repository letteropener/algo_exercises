'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''

def solution(A):
    # write your code in Python 3.6
    aux_list = [0]* len(A)
    for i in range(len(A)):
        if A[i] > 0 and A[i] <= len(A):
            aux_list[A[i]-1] = 1
    if 0 in aux_list: return aux_list.index(0)+1
    else: return len(A)+1