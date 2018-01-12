from sys import argv
from fft import fftPolyMult
import random, time

def bruteForcePolyMult(A, B):
	"""
	Performs the brute force polynomial multiplication algorithm.
	
	Args:
		A, B: (list) coefficients of polynomials
	Returns: (list) coefficients of their product, using the brute force algorithm
	"""

	n = len(A)
	C = [0] * n
	for k in range(n):
		for j in range(k+1):
			C[k] += A[j] * B[k-j]
	return C

def main(n):
	"""
	Driver program to demonstrate the brute force algorithm compared to
	the FFT algorithm.
	"""

	# generate two vectors of length n
	v1 = [random.random() for i in range(n)]
	v2 = [random.random() for i in range(n)]

	# pad with n zeros
	v1 += [0] * n
	v2 += [0] * n

	# brute force polynomial multiplication
	start1 = time.time()
	c1 = bruteForcePolyMult(v1, v2)
	end1 = time.time()
	t1 = end1 - start1

	# fast fourier transform polynomial multiplication
	start2 = time.time()
	c2 = fftPolyMult(v1, v2)
	end2 = time.time()
	t2 = end2 - start2

	# determine how to display the results
	if n <= 100:
		print('v1\n\n' + str(v1) + '\n\n')
		print('v2\n\n' + str(v2) + '\n\n')
		print('Brute Force Result:\n\n' + str(c1) + '\n\n')
		print('Fast Fourier Transform Result:\n\n' + str(c2) + '\n\n')
		print('Brute Force Run Time: ' + str(t1) + ' seconds')
		print('Fast Fourier Transform Run Time: ' + str(t2) + ' seconds')
	else:
		print('Brute Force Run Time: ' + str(t1) + ' seconds')
		print('Fast Fourier Transform Run Time: ' + str(t2) + ' seconds')
		with open('out.txt', 'w') as output:
			output.write('v1\n\n' + str(v1) + '\n\n')
			output.write('v2\n\n' + str(v2) + '\n\n')
			output.write('Brute Force Result:\n\n' + str(c1) + '\n\n')
			output.write('Fast Fourier Transform Result:\n\n' + str(c2) + '\n\n')
			output.write('Brute Force Run Time: ' + str(t1) + ' seconds\n')
			output.write('Fast Fourier Transform Run Time: ' + str(t2) + ' seconds')

if __name__ == "__main__":
	n = int(argv[1])
	main(n)
