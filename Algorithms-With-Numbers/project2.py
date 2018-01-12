from number_algorithms import *

def Problem1():
	n = input("\nEnter N, to test if it is prime: ")
	k = input("Enter K, the confidence level: ")
	p = isPrime(n, k)
	if p != -1:
		print('yes')
	else:
		print('no')

def Problem2():
	N = input("\nEnter N, the number of bits in the prime to be generated (N <= 50): ")
	K = input("Enter K, the confidence level: ")
	print(generatePrime(N, K))

def Problem3():
	n = input("\nEnter N, the number of bits in the primes to be generated: ")
	k = input("Enter K, the confidence level for generating primes, and the number of bits in E: ")
	rsa(n, k)

def main():
	while True:
		print('\nProblem 1: Test a number for primality')
		print('Problem 2: Generate a random prime number')
		print('Problem 3: RSA Encryption')
		choice = str(input("\nEnter 1, 2, or 3 for the problem you'd like to run (4 to quit): "))
		if choice == '1':
			print ("\nYou've chosen Problem 1")
			print('Your inputs should all be positive integers')
			Problem1()
		elif choice == '2':
			print("\nYou've chosen Problem 2")
			print('Your inputs should all be positive integers')
			Problem2()
		elif choice == '3':
			print("\nYou've chosen Problem 2")
			print('Your inputs should all be positive integers')
			Problem3()
		elif choice == '4':
			print ("\nQuitting")
			return
		else:
			print (">> Invalid input")

main()
