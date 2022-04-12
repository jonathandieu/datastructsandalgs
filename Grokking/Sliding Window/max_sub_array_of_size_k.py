# Given an array of positive numbers and a postive number k, find the maximum sum of any contiguous subarray of size 'k'
def brute_force_max_sub_array_of_size_k(k: int, arr: list) -> list:
    pass

def optimal_max_sub_array_of_size_k(k: int, arr: list) -> list:
    max_sum, window_sum = 0, 0 # Initialize window max and global max to zero
    window_start = 0 # define start index

    for window_end in range(len(arr)):

        window_sum += arr[window_end] # Add the next element and keep adding it until we reach k window size

        # Slide the window if we haven't hit the required window size 'k';
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start] # Subtract the element that's no longer in view of the window
            window_start += 1
    print(max_sum)

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  # Initialize maxes to 0
  window_sum = 0 # 6
  max_sum = 0 # 7
  window_start = 0 # 3

  # Loop through the length of the array with the window
  for window_end in range(len(arr)): # THISSSS IS WHERE N RUNTIME COMES FROM FOR LOOP ITERATIONS: 0 1 2 3 4
    window_sum += arr[window_end]

    # Check if the window has reached k size
    if (window_end + 1) >= k: # Plus 1 for indexing
      max_sum = max(window_sum, max_sum)
      window_sum -= arr[window_start]
      window_start += 1

  return max_sum

# driver function
if __name__ == "__main__":
    test_list = [2, 3, 4, 1, 5]
    # optimal_max_sub_array_of_size_k(2, test_list)
    print(max_sub_array_of_size_k(2, test_list))



# Runtime Analysis
# Go through the length of array: O(n)
# Space: No auxilliary data structures: O(1)

# list: [1, 2, 3, 4, 5]
# k = 1 answer = 5
# k = 2 answer = 9
