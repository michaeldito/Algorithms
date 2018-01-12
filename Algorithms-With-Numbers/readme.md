# Algorithms with Numbers

This was a project in my Analysis of Algorithms course where we 
implemented classic numerical algorithms while we were learning
about bit level operations. What made the project interesting was 
that we performed all of the operations using Python lists. We
called them "binary arrays" because the lists were used to simulate
bit level operations. The binary arrays were in little-endian, so
the list [0,0,1] was equal to 4.

Some implemented algorithms have two versions: one that accepts
lists as arguments, and another that accepts integers. The ones
that accept integers begin with an upper-case letter, and the other
begins with a lower-case letter.

## List of Algorithms
- *Shift*
  Shifts the binary array to the left or the right
- *Multiplication*
  Multiplies two binary arrays
- *Zero*
  Tests if a binary array is equal to 0
- *Floor Division by 2*
  Uses floor division to divide by 2
- *Even*
  Determines if the binary array is an even number
- *Addition*
  Adds two binary numbers together
- *Exclusive Or*
  Outputs True when the number of inputs with a value of 1 is odd
- *Next Carry*
  Returns True when the number of inputs with a value of 1 is >= 2
- *Binary to Decimal*
  Converts a binary array to a decimal
- *Decimal to Binary*
  Converts a decimal to a binary array
- *Reverse*
  Reverses a binary array
- *Trim*
  Trims any trailing zeros
- *Compare*
  Compares two binary arrays for equality, and if one is larger/smaller
- *Map*
  Returns an integer as a string for all binary arrays <= 9
- *Quotient*
  Returns the quotient when one binary array is divided by another
- *Divide*
  Returns the quotient and remainder when one binary array is divided
  by another
- *Subtract*
  Subtracts one binary array from another
- *Negation*
  Performs the negation of a binary array
- *Append Zeros*
  Appends zeros to a binary array
- *Exponentation*
  Performs exponentation of one binary array to the power of another
- *Greatest Common Denominator*
  Finds the greatest commond denominator of two binary arrays
- *Euclids Greatest Common Denominator*
  Performs the extended-euclid gcd on two binary arrays
- *Modulus*
  Performs the modulus of a % b
- *Modular Exponentation*
  Performs modular exponenetation of A^B mod N
- *Modular Inverse*
  Computes the modular inverse x, for ax % N = 1
- *Primality*
  Determines whether N is prime using Fermat's Little Theorem
- *Primality2*
  Determines whether N is prime by repeatedly calling primality k times
- *Primality3*
  Determines whether N is prime. First, we check if N is divisible by
  2, 3, 5, or 7, if so we can stop and return -1. If it is not, we
  move on to primality2 where we repeatedly call primality k times
- *Prime Number Generation*
  Generator for prime numbers
- *Generate a k-bit Integer*
  Gerneates a random binary array of length k
- *RSA Encryption*
  Performs RSA encryption