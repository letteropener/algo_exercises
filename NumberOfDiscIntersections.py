'''
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''
def solution(A):
    # write your code in Python 3.6
    n = len(A)
    start_point = []
    end_point = []
    for i in range(n):
        start_point.append(i - A[i] if i - A[i] > 0 else 0)
        end_point.append(i + A[i] if i+A[i] < n-1 else n-1)
    start_point.sort()
    end_point.sort()
    output = 0
    activatedIndex = 0
    deactivatedIndex = 0
    currentActive = 0

    for i in range(n):
        while activatedIndex < n and start_point[activatedIndex] <= end_point[deactivatedIndex]:
            activatedIndex += 1
            currentActive += 1
        currentActive -= 1
        output += currentActive
        if (output > 10000000): return -1
        deactivatedIndex += 1

    print(start_point)
    print(end_point)
    return output

def solution_BigOofN(A):
    # write your code in Python 3.6
    n = len(A)
    start_point = [0] * n
    end_point = [0] * n
    for i in range(n):
        start_point[i - A[i] if i - A[i] > 0 else 0] += 1
        end_point[i + A[i] if i+A[i] < n-1 else n-1] += 1
    print(start_point)
    print(end_point)
    t = 0
    total = 0
    for i in range(n):
        if start_point[i] > 0:
            total += t * start_point[i] + (start_point[i]-1)*start_point[i]//2
            if total > 10000000: return -1
            t += start_point[i]
        t -= end_point[i]
    return total


    print(start_point)
    print(end_point)
    return

# 3 + 3 + 2 + 2 + 1
#print(solution([1,5,2,1,4,0]))
print(solution_BigOofN([1,5,2,1,4,0]))