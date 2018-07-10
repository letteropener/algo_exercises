'''
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Assume that:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''

'''
We can use Kadane’s algorithm from two directions. First, we can safely ignore A[0] and A[N-1] since by definition they can’t be a part of any double-slice sum.

Now, define K1[i] as the maximum sum contiguous subsequence ending at index i, and similarly, define  K2[i] as the maximum sum contiguous subsequence starting with index i.

Then, iterate over i, and find the maximum sum of K1[i-1]+K2[i+1]. This is the max double slice sum.
'''

def solution(A):
    n = len(A)
    K1 = [0] * n
    K2 = [0] * n
    for i in range(1, n-1):
        K1[i] = max(K1[i-1]+A[i],0)
    for i in range(n-2,0,-1):
        K2[i] = max(K2[i+1]+A[i],0)
    max_value = 0
    for i in range(1,n-1):
        max_value = max(max_value,K1[i-1]+K2[i+1])
    return max_value

A = [-8, 10, 20, -5, -7, -4]
B = [3,2,6,-1,4,5,-1,-2,10,20,1]
C = [1,2,3,4,5]
D = [-5,-4,-3,-1,-2]
E = [3,-2,-1]
F = [-2, -3, -4, 1, -5, -6, -7]
G = [3,2,6,-1,4,5,-1,2]
H = [5,4,3,2,1]
print(solution(G))