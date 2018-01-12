def isSquare(N):
	n = getFloorSqrt(N)
	if (n * n == N):
		return True
	else:
		return False

def getFloorSqrt(N):
	if (N == 0 or N == 1):
		return N
	start = 0
	end = N // 2
	ans = 0
	while (start <= end):       # do a binary search for floor(sqrt(N))
		mid = (start + end) // 2
		if (mid * mid == N):      # is N a perfect square?
			return mid
		if (mid * mid < N):       # move closer to sqrt(N)
			start = mid + 1
			ans = mid
		else:
			end = mid - 1
	return ans
