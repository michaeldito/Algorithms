def knapsack(num_items, sack_size, weight, profit):
	if num_items == 0 or sack_size == 0:
		return 0
	
	# Add an extra column so we have sack_sizes from 0 up to and including sack_size
	table = [[0 for size in range(sack_size+1)] for item in range(num_items)]

	for item in range(num_items):
		for size in range(sack_size+1):
			if size == 0:
				table[item][size] = 0
			elif weight[item] > size:
				table[item][size] = table[item-1][size]
			else:
				table[item][size] = max(profit[item] + table[item-1][size-weight[item]], table[item-1][size])

	# Remember we added an extra column
	return table[num_items-1][sack_size]

def main():
	num_items = 10
	sack_size = 75
	weight = [5, 16, 10, 3, 14, 3, 15, 15, 17, 17]
	profit = [5, 14, 8, 5, 14, 3, 15, 13, 19, 16]
	max_profit = knapsack(num_items, sack_size, weight, profit)
	print('Max Profit = {}'.format(max_profit))

if __name__ == '__main__':
	main()
