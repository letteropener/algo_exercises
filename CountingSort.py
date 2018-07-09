def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in range(n):
        count[A[i]] += 1
    p = 0
    for i in range(k + 1):
        for j in range(count[i]):
            A[p] = i
            p += 1
    return A

print(countingSort([5,2,8,1,3,9],9))