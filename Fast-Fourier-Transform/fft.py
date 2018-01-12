from cmath import exp, pi

def fftPolyMult(A, B):
	"""
	Multiplies two vectors of coefficients of polynomials together using
	the FFT algorithm.
	
	Args:
		A, B: (list) coefficients of polynomials
	Returns: 
		(list) their product
	"""

	Fa = FFT(A, 0)
	Fb = FFT(B, 0)
	C = [Fa[i] * Fb[i] for i in range(len(A))]
	Fc = FFT(C, 0)
	Fc2 = [i.real for i in Fc]
	return IFT(Fc2)

def omega(k, n):
	"""
	The kth nth root of unity.

	Args:
		k: (int) indicates the kth nth root of unity
		n: (int) indicates the nth root of unity 
	Returns: 
		(complex) the kth nth root of unity
	"""

	return exp((2.0 * pi * 1j * k) / n)

def FFT(A, k):
	"""
	Performs the FFT algorithm.

	Args:
		A: (list) coefficients of a polynomial
		k: (int) indicates the kth nth root of unity, n is len(A)
	Returns: 
		(list) the point-value representation of the polynomial
	"""

	n = len(A)
	if n == 1:
		return A
	else:
		Ae = A[0::2]
		Ao = A[1::2]
		Fe = FFT(Ae, k+1)
		Fo = FFT(Ao, k+1)
		F = [0] * n
		for j in range(n//2):
			F[j] = Fe[j] + omega(j,n)*(Fo[j])
			F[j + (n//2)] = Fe[j] - omega(j,n)*(Fo[j])
		return F

def IFT(C):
	"""
	Performs the Inverse Fourier Transform.
	
	Args:
		C: (list) the point-value representation of a polynomial
	Returns: 
		(list) the coefficient representation of the polynomial
	"""

	return [i/float(len(C)) for i in [C[0]] + C[1::][::-1]]
