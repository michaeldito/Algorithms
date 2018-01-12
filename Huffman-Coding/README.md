# Mike Dito, Justin Bernard
# CS 415
# Final Project

## Huffman Coding Problem
Given a file of N bits in which P% of the bits are zero, and (100-P)% 
bits are one, how can we use Huffman's algorithm to compress this file?
Implement the algorithm and display the compression ratio achieved by
running it on randomly chosen binary strings of length 100,000.
Vary the value of P over the set {50, 60, 70, 80, 90} and output a 
table that shows the compression for each value of P.

## Solution
We decided to look at the bits in blocks of size b. Our program is 
written general enough so that we were able to test multiple values of b.
We also added additional output, in a clear format. That way we could
see exactly what bits were mapped to what codes, and their frequencies.
We varied b over the set { 2, 4, 8, 16, 20, 32, 35, 40, 50, 60, 100, 125, 
160, 200, 250, 400, 500, 625, 800, 1000 }. Decoder Bytes is roughly the
number of bytes the decoding dictionary takes up in memory. The purpose
of the decoding dictionary is to map huffman codes back to their original 
bits.

We thought, how would we decode this file later on if we didn't have the
huffman codes mapped to the original bits somewhere? So this metric let's
us see how many extra bits we'd need to save somwhere so that we could
compress the file later on.

## Files Included
- generatebits.py
  This file was used to randomly generate bits. The results of the output 
  are always within 0.1 of the expected output.

  Example results for 100,000 bits and P = 50:
    0: 0.50031
    1: 0.49969

- huffman.py
  This file implemented the huffman coding algorithm.

- node.py
  This file contains a Node class used in huffman.py

- data/
  These files contain the bit strings generated from generatebits.py

- bitfiles.txt
  This file contains the names of all 100000_bits_p_*.txt files

- ratio-results/
  These files contain the tables of data for each value of P.
  One table was generated for every value of b.

- compressed-data/
  These files contain the compressed data after running the program.

## How to run the program
We've provided input files, but if you would like to generate your
own with generatebits.py, you can do so by running:

  `python generatebits.py N P` 
  N = length of the bit string, P = % of 0's (0 < P < 100)

To run huffman.py:

  `python huffman.py bitfiles.txt`
