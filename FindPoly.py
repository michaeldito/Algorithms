from fft import fftPolyMult

def FindPoly(X):
  """
  Given a list of roots, this function will find it's polynomial.

  Args:
    X: (list) the roots, len(X) must be a power of 2
  Returns:
    (list) the coefficients of it's polynomial

  >>> FindPoly([1,1])
  [1, -2, 1, 0]
  """

  n = len(X)
  if n == 1:
    return [-X[0],1]
  a1 = FindPoly(X[:n//2])
  a2 = FindPoly(X[n//2:])
  a1 += [0] * n
  a2 += [0] * n
  a = fftPolyMult(a1, a2)
  a = [int(i) for i in a]
  return a
 