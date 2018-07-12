'''
This algorithm finds the gcd using only subtraction, binary representation, shifting and parity
testing. We will use a divide and conquer technique.
The following function calculate gcd(a, b, res) = gcd(a, b, 1) · res. So to calculate
gcd(a, b) it suffices to call gcd(a, b, 1) = gcd(a, b).

time complexity is O(log(a · b)) = O(log a + b) = O(log n). And for very large
integers, O((log n)^2), since each arithmetic operation can be done in O(log n) time.
'''
def gcd(a, b, res):
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd(a // 2, b // 2, 2 * res)
    elif (a % 2 == 0):
        return gcd(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd(a, b // 2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)


print(gcd(14, 26, 1))