import random
import sys
import time

sys.setrecursionlimit(10000000)

from random import *

def shift(A, n):
    """
    Shifts the binary array A n times.
    If n > 0 we right shift (multiply by 2).
    If n < 0 we left shift (floor divide by 2).

    Args:
        A: (list) a binary list
        n: (int) the amount to shift
    Returns:
        (list)

    >>> shift([1, 1, 1, 1], 1)
    [0, 1, 1, 1, 1]
    >>> shift([1, 1, 1, 1], -1)
    [1, 1, 1]
    >>> shift([1], 1)
    [0, 1]
    >>> shift([1], -1)
    [0]
    """

    if n == 0 and not A: return [0]
    if n == 0: return A
    if n > 0: return [0] + shift(A, n-1)
    if n < 0: return shift(A[:-1], n+1)

def mult(X, Y):
    """
    Multiplies two binary arrays, with the LSB stored in index 0.

    Args:
        X, Y: (list) binary arrays
    Returns:
        (list) binary array

    >>> A = [1, 1]
    >>> mult(A, A)
    [1, 0, 0, 1]
    """

    if zero(Y): return [0]
    Z = mult(X, div2(Y))
    if even(Y): return add(Z, Z)
    else: return add(X, add(Z, Z))

def Mult(X, Y):
    """
    Multiplies two integers.

    Args:
        X, Y: (int)
    Returns:
        (int)

    >>> Mult(2, 2)
    4   
    """

    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(mult(X1,Y1))

def zero(X):
    """
    Test if a binary array is 0. Both [] and [0, 0, ..., 0] represent 0.

    Args:
        X: (list) binary array
    Returns:
        (bool)
    
    >>> zero([0])
    True
    >>> zero([0,0,0])
    True
    """

    if len(X) == 0: return True
    else: 
        for bit in X: 
            if bit == 1: return False
    return True

def div2(Y):
    """
    Floor divides Y by 2.

    Args:
        Y: (list) binary array
    Returns:
        (list) binary array

    >>> div2([1,1,1])
    [1, 1]
    """
    if len(Y) == 0: return Y
    else: return Y[1:]

def even(X):
    """
    Determines if X is an even number.

    Args:
        X: (list) binary array
    Returns:
        (bool)

    >>> even([1])
    False
    >>> even([0,1])
    True    
    """

    if ((len(X) == 0) or (X[0] == 0)): return True
    else: return False

def add(A, B):
    """
    Adds A and B.

    Args:
        A, B: (list) binary array
    Returns
        (list) binary array

    >>> add([1,1], [1,1])
    [0, 1, 1]   
    """

    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)
    if n < m:
        A1 += [0] * (m - n)
    else:
        B1 += [0] * (n - m)
    N = max(m, n)
    C = []
    carry = 0
    for j in range(N):
        C.append(exc_or(A1[j], B1[j], carry))
        carry = nextcarry(carry, A1[j], B1[j])
    if carry == 1:
        C.append(carry)
    return C

def Add(A,B):
    """
    Adds A and B.

    Args:
        A, B: (int)
    Returns
        (int)

    >>> Add(10,100)
    110  
    """

    return bin2dec(add(dec2bin(A), dec2bin(B)))

def exc_or(a, b, c):
    """
    Exclusive Or outputs True when the number of 1 inputs is odd, False otherwise.

    Args:
        a, b, c: (int)
    Returns:
        (bool)

    >>> exc_or(1,0,0)
    1
    >>> exc_or(0,1,0)
    1
    >>> exc_or(0,0,1)
    1
    >>> exc_or(1,1,1)
    1
    >>> exc_or(0,0,0)
    0
    >>> exc_or(1,1,0)
    0
    >>> exc_or(0,1,1)
    0
    >>> exc_or(1,0,1)
    """

    return (a ^ (b ^ c))

def nextcarry(a, b, c):
    """
    Next Carry returns True when the number of 1 inputs is >= 2.

    Args:
        a, b, c: (int)
    Returns:
        (bool)
    
    >>> nextcarry(0,0,0)
    0
    >>> nextcarry(1,0,0)
    0
    >>> nextcarry(0,1,0)
    0
    >>> nextcarry(0,0,1)
    0
    >>> nextcarry(0,1,1)
    1
    >>> nextcarry(1,0,1)
    1
    >>> nextcarry(1,1,0)
    1
    >>> nextcarry(1,1,1)
    1
    """

    if ((a & b) | (b & c) | (c & a)): return 1
    else: return 0

def bin2dec(A):
    """
    Converts a binary array to an integer.

    Args:
        A: (list) binary array
    Returns:
        (int)

    >>> bin2dec([1,1,1])
    7
    """

    if len(A) == 0:
        return 0
    val = A[0]
    pow = 2
    for j in range(1, len(A)):
        val = val + pow * A[j]
        pow = pow * 2
    return val

def reverse(A):
    """
    Reverses a binary array.

    Args:
        A: (list) binary array
    Returns:
        (list) binary array

    >>> reverse([1,1,0,0])
    [0, 0, 1, 1]    
    """

    return A[::-1]

def trim(A):
    """
    Trims any trailing zeros.

    Args:
        A: (list) binary array
    Returns:
        (list) binary array

    >>> trim([1,1,0,0])
    [1, 1]
    >>> trim([0,0,1,1])
    [0, 0, 1, 1]    
    """

    if len(A) == 0:
        return A
    A1 = reverse(A)
    while ((not (len(A1) == 0)) and (A1[0] == 0)):
        A1.pop(0)
    return reverse(A1)

def trim2(A):
    """
    Trims any trailing zeros.

    Args:
        A: (list) binary array
    Returns:
        (list) binary array

    >>> trim2([1,1,0,0])
    [1, 1]
    >>> trim2([0,0,1,1])
    [0, 0, 1, 1]    
    """

    if len(A) == 0:
        return A
    while A[-1] == 0:
        A.pop()
    return A

def compare(A, B):
    """
    Compares A and B and outputs:
    1 if A > B
    2 if B > A
    0 if A == B

    Args:
        A, B: (list) binary array
    Returns:
        (int)

    >>> compare([0], [1])
    2
    >>> compare([1], [0])
    1
    >>> compare([1], [1])
    0
    """

    A1 = reverse(trim(A))
    A2 = reverse(trim(B))
    if len(A1) > len(A2):
        return 1
    elif len(A1) < len(A2):
        return 2
    else:
        for j in range(len(A1)):
            if A1[j] > A2[j]:
                return 1
            elif A1[j] < A2[j]:
                return 2
        return 0

def Compare(A, B):
    """
    Compares A and B and outputs:
    1 if A > B
    2 if B > A
    0 if A == B

    Args:
        A, B: (int)
    Returns:
        (int)

    >>> Compare(1,1)
    0
    >>> Compare(1,0)
    1
    >>> Compare(0,1)
    2
    """

    return compare(dec2bin(A), dec2bin(B))

def dec2bin(n):
    """
    Converts an integer into a binary array.

    Args:
        n: (int)
    Returns:
        (list) binary array

    >>> dec2bin(8)
    [0, 0, 0, 1]   
    """

    if n == 0:
        return []
    m = n/2
    A = dec2bin(m)
    fbit = n % 2
    return [fbit] + A

def map(v):
    """
    Returns an integer as a string for all binary arrays <= 9.

    Args:
        v: (list) binary array
    Returns:
        (str)

    >>> map([1,1,1])
    '7'
    """

    if v == []:
        return '0'
    elif v == [0]:
        return '0'
    elif v == [1]:
        return '1'
    elif v == [0,1]:
        return '2'
    elif v == [1,1]:
        return '3'
    elif v == [0,0,1]:
        return '4'
    elif v == [1,0,1]:
        return '5'
    elif v == [0,1,1]:
        return '6'
    elif v == [1,1,1]:
        return '7'
    elif v == [0,0,0,1]:
        return '8'
    elif v == [1,0,0,1]:
        return '9'

def bin2dec1(n):
    """
    Converts a binary array to a decimal.

    Args:
        n: (list) binary array
    Returns:
        (int)

    >>> bin2dec1([1,1,1])
    '7'
    """

    if len(n) <= 3:
        return map(n)
    else:
        temp1, temp2 = divide(n, [0,1,0,1])
        return bin2dec1(trim(temp1)) + map(trim(temp2))

def quotient(X, Y):
    """
    Returns the quotient when X is divided by Y.

    Args:
        X, Y: (list) binary array
    Returns:
        (list) binary array

    >>> quotient([0,1], [1])
    [0, 1]
    >>> quotient([0,1], [0,1])
    [1]   
    """
    (q, r) = divide(X, Y)
    return q

def Quotient(X, Y):
    """
    Returns the quotient when X is divided by Y.

    Args:
        X, Y: (int)
    Returns:
        (int)

    >>> Quotient(4,2)
    2   
    """
    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(quotient(X1, Y1))

def divide(X, Y):
    """
    Finds the quotient and remainder when X is divided by Y

    Args:
        X, Y: (list) binary array
    Returns:
        (tuple)

    >>> divide([0,0,1], [0,1])
    ([0, 1], [0])   
    """

    if zero(X):
        return ([],[])
    (q,r) = divide(div2(X), Y)
    q = add(q, q)
    r = add(r, r)
    if (not even(X)):
        r = add(r,[1])
    if (not compare(r,Y) == 2):
        r = sub(r, Y)
        q = add(q, [1])
    return (q,r)

def Divide(X, Y):
    """
    Finds the quotient and remainder when X is divided by Y

    Args:
        X, Y: (list) binary array
    Returns:
        (tuple)

    >>> Divide(16, 4)
    (4, 0)
    """

    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    (q,r) = divide(X1, Y1)
    return (bin2dec(q), bin2dec(r))

def sub(A,B):
    """
    Subtracts B from A. Handles a negative result by returning it as
    a positive number.
    
    Args:
        A, B: (list) binary array
    Returns:
        (list) binary array

    >>> sub([1,1,1,1], [1,0,1])
    [0, 1, 0, 1]  
    >>> sub([1,0,1], [1,1,1,1])
    [0, 1, 0, 1]  
    """

    A1 = A[:]                              # first make a copy of A
    B1 = B[:]                              # first make a copy of B
    c = compare(A1, B1)                    # is A > B, A < B, or A == B?
    if (c == 0):                           # if A == B
        return [0]                         # just return [0]
    maxL = max(len(A1), len(B1))           # get length of longest binary array
    ld = len(A1) - len(B1)                 # get the difference of their lengths
    if (ld > 0):                           # if A has more bits than B
        B1 = appendZeroes(B1, ld)          # add extra zeroes to B
    if (ld < 0):                           # if B has more bits than A
        A1 = appendZeroes(A1, abs(ld))     # add extra zeroes to A
    B1 = flipBits(B1)                      # flip B's bits
    B1 = add(B1, [1])                      # add 1 to B
    if (len(B1) > maxL):                   # if B has the carry bit set
        B1.pop()                           # get rid of it
    result = add(A1, B1)                   # add A and B
    if (len(result) > maxL):               # if the result has the carry bit set
        result.pop()                       # get rid of it
    if (c == 1):                           # if A > B
        return result                      # return result
    else:                                  # B > A, result will be negative
        result = sub(result, [1])       # subtract 1 from result
        result = flipBits(result)       # flip result's bits
        if (len(result) > maxL):        # if result has the carry bit set
            result.pop()                # get rid of it
        return result                   # return result (as positive number)

def Sub(A, B):
    """
    Subtracts B from A. Handles a negative result by returning it as
    a positive number.
    
    Args:
        A, B: (int)
    Returns:
        (int)

    >>> Sub(100, 50)
    50
    """

    A1 = dec2bin(A)
    B1 = dec2bin(B)
    return bin2dec(sub(A1, B1))

def flipBits(A):
    """
    Performs the negation of all bits in A.

    Args:
        A: (list) binary array
    Returns
        A: (list) binary array

    >>> flipBits([1,0,1])
    [0, 1, 0]
    """

    for i in range(len(A)):
        if A[i] == 1: 
            A[i] = 0
        else: 
            A[i] = 1
    return A

def negate(A):
    """
    Performs the negation of all bits in A.

    Args:
        A: (list) binary array
    Returns
        A: (list) binary array

    >>> negate([1,0,1])
    [0, 1, 0]
    """
    return [0 if bit == 1 else 1 for bit in A]

def appendZeroes(A, n):
    """
    Appends n zeros to A.

    Args:
        A: (list) binary array
        n: (int)
    Returns:
        A: (list) binary array
    
    >>> appendZeroes([],5)
    [0, 0, 0, 0, 0]
    """

    for i in range(n):
        A.append(0)
    return A

def exp(X, Y):
    """
    Performs exponentiation of X to the Y power.

    Args:
        X, Y: (list) binary array
    Returns:
        (list) binary array

    >>> exp([0,1], [0,1])
    [0, 0, 1]    
    """

    if zero(Y):
        return [1]
    z = exp(X, div2(Y))
    if even(Y):
        return mult(z, z)
    else:
        return mult(X, mult(z, z))

def Exp(X, Y):
    """
    Performs exponentiation of X to the Y power.

    Args:
        X, Y: (int)
    Returns:
        (int)

    >>> Exp(2, 8)
    256   
    """

    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(exp(X1, Y1))

def gcd(a, b):
    """
    Finds the greatest common denominator of a and b.

    Args:
        a, b: (list) binary array
    Returns:
        (list) binary array

    >>> gcd([0,0,1], [0, 0, 0, 0, 1])
    [0, 0, 1]
    """

    if (zero(b) or (compare(a, b) == 0)):
        return a
    if compare(a, b) == 2:
        return gcd(b, a)
    else:
        return gcd(b, mod(a, b))

def Gcd(a, b):
    """
    Finds the greatest common denominator of a and b.

    Args:
        a, b: (int)
    Returns:
        (int)

    >>> Gcd(127, 9)
    1
    >>> Gcd(64,8)
    8
    """

    a1 = dec2bin(a)
    b1 = dec2bin(b)
    return bin2dec(gcd(a1, b1))

def egcd(a, b, s):
    """
    Performs the extended-euclid gcd.
    
    Args:
        a, b: (list) binary array
        s: (int) sign bit
    Returns:
        x, y, d, s: (tuple)
    """

    c = compare(a, b)
    (x, y, d, s) = egcd2(a, b, s)
    if c == 2: # b > a
        if s == 2:
            s = 1
        elif s == 1:
            s = 2
        return (y, x, d, s)
    else:
        return (x, y, d, s)

def egcd2(a, b, s):
    """
    Performs the extended-euclid gcd.
    
    Args:
        a, b: (list) binary array
        s: (int) sign bit
    Returns:
        x, y, d, s: (tuple)
    """

    if zero(b) or compare(a, b) == 0:
        return ([1], [0], a, 0)
    c = compare(a, b)
    if c == 2:
        return egcd2(b, a, s)
    (x, y, d, s) = egcd(b, mod(a, b), 0)
    aDivB = quotient(a, b)
    aDivBxY = mult(aDivB, y)
    if s == 0:                       # x and y are positive
        if compare(x, aDivBxY) == 2: # aDivBxY > x --> y will be negative
            s = 2
        else:                        # aDivBxY <= x --> x, y both are positive
            s = 0
        return (y, sub(x, aDivBxY), d, s)
    elif s == 1:                     # x is negative --> -x - aDivBxY = y is negative
        s = 2                        # y will be negative
    else:                            # y is negative --> x - -aDivBXy = y is positive
        s = 1                        # but x will be negative
    return (y, add(x, aDivBxY), d, s)

def Egcd(a, b, s):
    """
    Performs the extended-euclid gcd.
    
    Args:
        a, b: (int)
        s: (int) sign bit
    Returns:
        x, y, d, s: (tuple)
    """

    a1 = dec2bin(a)
    b1 = dec2bin(b)
    return egcd(a1, b1, s)

def mod(a, b):
    """
    Performs the modulus of a % b.

    Args:
        a, b: (list) binary array
    Returns:
        r: (list) binarry array - remainder

    >>> mod([1,1,1], [0,1])
    [1, 0]
    """

    (q,r) = divide(a, b)
    return r

def Mod(a, b):
    """
    Performs the modulus of a % b.

    Args:
        a, b: (list) binary array
    Returns:
        r: (int) - remainder

    >>> Mod(22, 4)
    2
    """

    a1 = dec2bin(a)
    b1 = dec2bin(b)
    return bin2dec(mod(a1, b1))

def modexp(A, B, N):
    """
    Performs modular exponenetation of A^B mod N.

    Args:
        A, B, N: (list) binary array
    Returns:
        (list) binary array

    >>> modexp([1, 0, 1], [1], [1, 1, 0, 0, 1])
    [1, 0, 1]
    """

    if (zero(B)):
        return [1]
    else:
        B1 = div2(B)
        Z = modexp(A, B1, N)
        if even(B):
            return mod(mult(Z, Z), N)
        else:
            return mod(mult(A, mult(Z, Z)), N)

def Modexp(A, B, N):
    """
    Performs modular exponenetation of A^B mod N.

    Args:
        A, B, N: (list) binary array
    Returns:
        (int)

    >>> Modexp(5, 1, 19)
    5
    """

    A1 = dec2bin(A)
    B1 = dec2bin(B)
    N1 = dec2bin(N)
    return bin2dec(modexp(A1, B1, N1))

def modinv(a, n):
    """
    Computes the modular inverse, x.
    ax % N = 1

    Args:
        a, b: (list) binary array
    Returns:
        (list) binary array

    >>> modinv([1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1])
    [0, 1, 1]
    """

    (x, y, d, s) = egcd(a, n, 0)
    if compare(d, [1]) != 0:
        return []
    temp = mod(x,n)
    if s == 2:
        return temp
    else:
        temp = sub(x, mult(add(quotient(x, n),[1]), n))
        return temp

def modinv2(a, n):
    """
    Computes the modular inverse of a^(-1) mod n.

    Args:
        a, b: (list) binary array
    Returns:
        (list) binary array

    >>> modinv2([1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1])
    [0, 1, 1]
    """
    (x, y, d, s) = egcd(a, n, 0)
    if compare(d, [1]) != 0:
        return []
    if s == 1:
        return sub(x, mult(add(quotient(x, n),[1]), n))
    return x

def Modinv(a, n):
    """
    Computes the modular inverse of a^(-1) mod n.

    Args:
        a, b: (int)
    Returns:
        (int)

    >>> Modinv(31, 37)
    6
    """

    a1 = dec2bin(a)
    n1 = dec2bin(n)
    return bin2dec(modinv2(a1, n1))

def primality(N):
    """
    Determines whether N is prime using Fermat's Little Theorem.

    Args:
        N: (list) binary array
    Returns:
        If N is prime, it returns N (list)
        If N is not prime, it returns -1 (int)

    >>> primality(7)
    7
    >>> primality(8)
    -1
    """

    a = randint(2, N)
    if Modexp(a, N - 1, N) == 1:
        return N
    else:
        return -1

def primality2(N, k):
    """
    Determines whether N is prime by repeatedly calling primality k times.
    If any call results in primality returning a number that is not -1, then
    N is a prime number and we should return it's value.

    Args:
        N: (int) the number to check for primality
        k: (int) our confidence level
    
    Returns:
        If N is prime, return it's value
        If N is not prime, return -1

    >>> primality2(90000,7)
    -1
    """

    for i in range(0, k):
        p = primality(N)
        if p != -1:
            return p
    return -1

def primality3(N, k):
    """
    Determines whether N is prime. First, we check if N is divisible by
    2, 3, 5, or 7, if we can stop and return -1. If it is not, we move on to 
    primality2 where we repeatedly call primality k times. If any call 
    results in primality returning a number that is not -1, then
    N is a prime number and we should return it's value.

    Args:
        N: (int) the number to check for primality
        k: (int) our confidence level, used in primality2
    Returns:
        If N is prime, return N
        If N is not prime, return -1

    >>> primality3(541,7)
    541
    >>> primality3(8,8)
    -1
    """

    values = [2, 3, 5, 7]
    for i in range(len(values)):
        if zero(dec2bin(Mod(N, values[i]))):
            return -1
    return primality2(N, k)

def isPrime(N, k):
    """
    Wrapper for primality3.
    """

    return primality3(N, k)

def generatePrime(n, k):
    """
    Generator for prime numbers.

    Args:
        n: (int) - length of the binary array
        k: (int) - confidence level
    Returns:
        (int)

    >>> generatePrime(10,10)
    863
    """

    if n > 50:
        print('n should be <= 50')
        return -1
    kbits = generateKBitInt(n)
    a = primality3(bin2dec(kbits), k)
    if a == -1:
        return generatePrime(n, k)
    else:
        return a

def generateKBitInt(K):
    """
    Generates a random binary array of length K.

    Args:
        K: (int) - the length of the binary array
    Returns:
        (list) binary array

    >>> generateKBitInt(10)
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    """
    
    k = []
    for i in range(K - 2):
        k.append(randint(0,1))
    k = [1] + k + [1]
    return k

def rsa(n, k):
    """
    Performs RSA encryption.

    Args:
        n: (int) - the length of the two prime numbers created
        k: (int) - the confidence level
    Outputs:
        Encrypted and Decrypted messages.
    Returns:
        Nothing

    >>> rsa(5,5)
    Enter a message (an integer): 123
    Encrypted Message: 309
    Decrypted Message: 123
    """

    p = generatePrime(n, k)
    q = generatePrime(n, k)
    N = Mult(p, q)
    E = []
    gcd_ = []
    while compare(gcd_, [1]) != 0:
        E = generateKBitInt(n)
        gcd_ = gcd(E, dec2bin(Mult(Sub(p, 1), Sub(q, 1))))
    D = Modinv(bin2dec(E), Mult(Sub(p, 1), Sub(q, 1)))
    M = input("Enter a message (an integer): ")
    Em = modexp(dec2bin(M), E, dec2bin(N))
    print('Encrypted Message: ' + str(bin2dec(Em)))
    Dm = modexp(Em, dec2bin(D), dec2bin(N))
    print('Decrypted Message: ' + str(bin2dec(Dm)))
