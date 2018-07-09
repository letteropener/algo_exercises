'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
'''

def solution(A):
    # write your code in Python 3.6
    counter = 0
    tmp_value = -1
    for i in A:
        if counter == 0:
            tmp_value = i
            counter += 1
        else:
            if i == tmp_value:
                counter += 1
            else:
                counter -= 1
    leader_candidate = -1
    if counter > 0:
        leader_candidate = tmp_value
    leader_counter = 0
    leader = -1
    for i in A:
        if i == leader_candidate:
            leader_counter += 1
        if leader_counter > (len(A) // 2):
            leader = leader_candidate
            return A.index(leader)
    return leader