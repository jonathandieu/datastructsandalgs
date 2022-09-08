def num_subarray_less_than_k(nums, k: int) -> int:
	# Initialize variables we need
	result = 0
	product = 1
	window_start = 0
	# We automatically increment through window_start
	for window_end in range(len(nums)):
		product *= nums[window_end]
		# This is where we move our window_start
		while product >= k and window_start <= window_end:
			product /= nums[window_start]
			window_start += 1
			result += window_end - window_start + 1
	return result
