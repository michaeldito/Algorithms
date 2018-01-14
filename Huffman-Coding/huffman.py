from heapq import heappush, heappop
from argparse import ArgumentParser
from node import *
import pandas
import sys

BIT_BLOCK = 0
DEBUG = True

def map_bits_to_freq(bit_string):
  """
  Scan through the bit_string BIT_BLOCK at a time. Along the way, keep track
  of the frequency that each bit substring occurs.

  Args:
    bit_string: (str) the bit string to scan.
  Returns: 
    bits_to_freq: (dict) bit substrings mapped to their frequencies.
  """
  start = 0
  end = BIT_BLOCK
  bits_to_freq = {}
  n = len(bit_string)
  while start < n:
    bits = bit_string[start:end]
    if bits in bits_to_freq:
      bits_to_freq[bits] += 1
    else:
      bits_to_freq[bits] = 1
    start += BIT_BLOCK
    end += BIT_BLOCK  
  return bits_to_freq

def build_huffman_tree(min_heap):
  """
  Build a Huffman Tree from a min-heap.

  Args:
    min_heap: (list) the min heap represented as a list.
  Returns:
    min_heap[0]: (node) the root of the Huffman Tree.
  """
  while len(min_heap) > 1:
    min_node_a = heappop(min_heap)
    min_node_b = heappop(min_heap)
    value = min_node_a.value + min_node_b.value
    huffman_node = Node(None, value, min_node_a, min_node_b)
    heappush(min_heap, huffman_node)
  return min_heap[0]
 
def get_huffman_codes(code, node, huffman_codes):
  """
  Traverse the Huffman Tree and along the way map the key of each node
  to it's huffman code.

  Args:
    code: (str) the current value of the code.
    node: (node) the root of the Huffman Tree.
    huffman_codes: (dict) is a map of node values to their codes.
  """
  if node.get_key() != None:
    if code == "":
      huffman_codes[node.get_key()] = "0"
    else:
      huffman_codes[node.get_key()] = code
  else:
    get_huffman_codes(code + "0", node.get_left_child(), huffman_codes)
    get_huffman_codes(code + "1", node.get_right_child(), huffman_codes)

def encode(bit_string, huffman_codes):
  """
  Encodes bit_string using the huffman codes.
  Get the huffman code for each bit substring and concatenate it to a new string.

  Args:
    bit_string: (str) the string to encode.
    huffman_codes: (dict) map of bit substrings to their codes.
  Returns:
    encoded_string: (str) the encoded string.
  """
  start = 0
  end = BIT_BLOCK
  n = len(bit_string)
  encoded_string = ""
  while start < n:
    bits = bit_string[start:end]
    encoded_string += huffman_codes[bits]
    start += BIT_BLOCK
    end += BIT_BLOCK
  return encoded_string

def decode(encoded_string, codes_to_bits):
  """
  Decode encoded_string back to it's original form.

  Args:
    encoded_string: (str) the string to decode.
    codes_to_bits: (dict) map of huffman codes to the original bits

  Returns:
    decoded_string: (str) the original string.
  """
  start = 0
  end = 1
  n = len(encoded_string)
  decoded_string = ""
  while start < n:
    code = encoded_string[start:end]
    if code in codes_to_bits:
      decoded_string += codes_to_bits[code]
      start = end
    end += 1
  return decoded_string

def populate_min_heap(bits_to_freq):
  """
  Populate the min heap with our frequency counts.

  Args:
    bits_to_freq: (dict) map of bits to their frequency counts.

  Returns:
    min_heap: (heapq) a min heap with nodes being bits and their frequency.
  """
  min_heap = []
  for key, value in bits_to_freq.items():
    node = Node(key, value, left=None, right=None)
    heappush(min_heap, node)
  return min_heap

def huffman_coding(bit_string, P):
  """
  Performs the Huffman Coding algorithm on a bit string.
  Prints out a table of the original bits, their frequencies, and codes.
  Runs a decode test.

  Args:
    bit_string: (str) the string to encode.
    P: (str) the percentage of zeros in the bit string.

  Returns:
    encoded_string: (str) the encoded string.
    decoder_bytes: (bytes) the number of bytes in the decoder map.
  """
  bits_to_freq = map_bits_to_freq(bit_string)
  
  min_heap = populate_min_heap(bits_to_freq)
  huffman_tree = build_huffman_tree(min_heap)
  huffman_codes = {}
  get_huffman_codes("", huffman_tree, huffman_codes)
  encoded_string = encode(bit_string, huffman_codes)

  bits = []
  freqs = []
  codes = []
  for b, f in bits_to_freq.iteritems():
    bits.append(b)
    freqs.append(f)
    codes.append(huffman_codes[b])

  data = { 'Bits' : bits, 'Frequency': freqs, 'Codes': codes }
  df = pandas.DataFrame(data=data)

  print('+-----------------------------------------------------------------------+')
  print('| Bits, Codes, and Frequency Counts for P: {}, BIT_BLOCK: {}\t\t|'.format(P, str(BIT_BLOCK)))
  print('+-----------------------------------------------------------------------+')
  print('')
  print(df)

  codes_to_bits = dict((huffman_codes.get(key, key), key) for (key, value) in bits_to_freq.items())
  decoded_string = decode(encoded_string, codes_to_bits)
  if bit_string == decoded_string:
    print('\nHuffman Decoding Test: Passed\n')
  else:
    print('\nHuffman Decoding Test: Failed\n')
  
  decoder_bytes = sys.getsizeof(codes_to_bits)

  return encoded_string, decoder_bytes

def main(file_name):
  """
    Given a filename containing the names of all file to encode, main
    will encode them all and print out a table of data about each
    encoding.
  """
  compression_ratios = []
  decoder_byte_sizes = []
  original_bit_lengths = []
  encoded_bit_lengths = []
  P = ['50', '60', '70', '80', '90']

  p_idx = 0

  with open(file_name, 'r') as f:
    file_names = f.readlines()
    file_names = [file_name.strip() for file_name in file_names]
    for file_name in file_names:
      bit_string = open('data/{}'.format(file_name), 'r').read()
      encoded_string, decoder_bytes = huffman_coding(bit_string, P[p_idx])
      compression_ratio = float(len(bit_string)) / float(len(encoded_string))

      original_bit_lengths.append(len(bit_string))
      encoded_bit_lengths.append(len(encoded_string))
      compression_ratios.append(compression_ratio)
      decoder_byte_sizes.append(decoder_bytes)
      
      with open('compressed-data/{}-compressed-data-{}-bit-blocks.txt'.format(file_name, str(BIT_BLOCK)), 'w') as compressed_file:
        compressed_file.write(encoded_string)

      p_idx += 1

  df = pandas.DataFrame(data={
    'P': P, 
    'Original Bit Lengths': original_bit_lengths,
    'Encoded Bit Lengths': encoded_bit_lengths,
    'Ratio': compression_ratios, 
    'Decoder Bytes': decoder_byte_sizes
    })
  print('+-----------------------------------------------------------------------+')
  print('|\t\tCompression Results with {} BIT_BLOCK\t\t\t|'.format(str(BIT_BLOCK)))
  print('+-----------------------------------------------------------------------+')
  print(df)
  print('')

  with open('ratio-results/compression-ratios-with-{}-bit-blocks.txt'.format(str(BIT_BLOCK)), 'w') as ratios_file:
    ratios_file.write('Compression Results with {} Bit Blocks\n\n'.format(str(BIT_BLOCK)))
    ratios_file.write(str(df))
 
if __name__ == "__main__":
  parser = ArgumentParser(description='This script will compress files of bits using Huffman Coding')
  parser.add_argument('file_name', help='The file that contains names of all files to compress')
  args = parser.parse_args()
  bits = [2, 4, 8, 16, 20, 32, 35, 40, 50, 60, 100, 125, 160, 200, 250, 400, 500, 625, 800, 1000]
  for bit in bits:
    BIT_BLOCK = bit
    start = raw_input("Hit enter to compress using {} bit blocks:\n".format(str(bit)))
    main(args.file_name)
