import random
from argparse import ArgumentParser

def generate_bits(N, P):
  weighted_choices = [(0, P), (1, 100-P)]
  population = [v for v, count in weighted_choices for i in range(count)]
  ones = 0
  zeroes = 0
  with open('{}_bits_p_{}.txt'.format(N, P), 'w') as file:
    for i in range(N):
      choice = random.choice(population)
      if choice == 1:
        ones += 1
      else:
        zeroes += 1
      file.write(str(choice))

  percentZero = float(zeroes) / float(N)
  percentOne = float(ones) / float(N)
  print('0: {}'.format(str(percentZero)))
  print('1: {}'.format(str(percentOne)))

def main(N, P):
  generate_bits(N, P)

if __name__ == "__main__":
  parser = ArgumentParser(description='This script will generate a string of N bits \
    where P % are 0 and 100-P % are 1')
  parser.add_argument('N', help='The length of the bit string')
  parser.add_argument('P', help='The percent of 0s')
  args = parser.parse_args()
  main(int(args.N), int(args.P))