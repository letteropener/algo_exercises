'''
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''


def leader_checker(A, leader_candidate):
    leader_counter = 0
    leader = -1
    for i in A:
        if i == leader_candidate:
            leader_counter += 1
        if leader_counter > (len(A) // 2):
            leader = leader_candidate
    return leader,leader_counter


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

    leader,total_count = leader_checker(A, leader_candidate)
    if leader == -1:
        return 0
    else:
        equiLeader = 1 if A[0] == leader and len(A) > 1 else 0
        count_left = 1 if A[0] == leader else 0
        count_right = total_count if A[0] != leader else total_count-1
        for i in range(1,len(A)):
            if A[i] == leader:
                count_left += 1
                count_right -= 1
            if count_left > (i+1)//2 and count_right > (len(A)-i-1) // 2:
                equiLeader += 1
        return equiLeader

print(solution([0]))