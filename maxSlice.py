'''
Let’s define a problem relating to maximum slices. You are given a sequence of n integers
a0, a1,...,an-1 and the task is to find the slice with the largest sum. More precisely, we are
looking for two indices p, q such that the total ap + ap+1 + ... + aq is maximal. We assume
that the slice can be empty and its sum equals 0.

[5,-7,3,5,-2,4,-1]   => max slice [3,5,-2,4]

the slice with the largest sum is highlighted in gray. The sum of this slice
equals 10 and there is no slice with a larger sum. Notice that the slice we are looking for may
contain negative integers, as shown above
'''

def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

print(golden_max_slice([5,-7,3,5,-2,4,-1] ))