from math import sqrt

def isPower(N):
    if (N <= 1):
        return True
    sqrtN = int(sqrt(N))
    for i in range(2, sqrtN+1):
        p = i
        while (p <= N):
            p = p * i
            if (p == N):
                return True
    return False

'''
sqrt(N) takes O(log N) to compute.             // O(log N)
iterate from 2 -> sqrtN.                       // O(N)
    multiply p by i at most sqrt(N) - 2 times. // O(sqrtN - 2), so O(N)

Overall: O(log N) + O(N) * O(N) = O(N^2)
'''
