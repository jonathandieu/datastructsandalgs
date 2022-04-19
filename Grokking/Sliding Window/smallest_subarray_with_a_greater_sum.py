def smallest_subarray_with_a_greater_sum(arr: list, S: int):
    """
    Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
    """
    # Initialize global min to be a number we never reach and window_sum
    min_size = len(arr) + 1 # answer we are returning
    window_size = 0 # compare to the min_size each time
    window_sum = 0 # gets compared to S      7!
    window_start = 0 # Butt of the catepillar

    #               0  1  2  3  4  5 Indices of the array
    # test_list1 = [7, 1, 5, 2, 3, 2] S = 7 EXPECTED = 1
    # test_list2 = [2, 1, 5, 2, 3, 2] EXPECTED = 2
    #

    # For loop to move the window along, end being the index in range()
    for window_end in range(len(arr)): # 0, 1, 2, 3, 4, 5
        window_sum += arr[window_end] # arr[0] = 7
        window_size += 1
        if window_sum >= S:
            min_size = min(window_size, min_size)
            window_sum -= arr[window_start]
            window_start += 1
            window_size -= 1
            if window_sum >= 7:
                min_size = min(min_size, window_size)



    return min_size

def smallest_subarray_sum(arr, s):
    min_size = len(arr) + 1 # answer we are returning (initialized to something we'll never reach)
    window_size = 0 # compare to the min_size each time
    window_sum = 0 # gets compared to S      !
    butt = 0 # butt of the caterpillar
    for head in range(len(arr)): # Moving the catepillar's head 0, 1, 2, 3, 4, 5
        window_sum += arr[head] # 12
        window_size = (head - butt) + 1 #4
        while window_sum >= s:
            min_size = min(window_size, min_size) # 3
            window_sum -= arr[butt] # 5
            butt += 1 # 1
            window_size -= 1 # 3
    return min_size


if __name__=="__main__":
    test_list2 = [7, 1, 5, 2, 3, 2]
    test_list1 = [2, 1, 5, 2, 3, 8]
    # print(smallest_subarray_with_a_greater_sum(test_list2, 7), "Expected: 1")
    print("output:", smallest_subarray_with_a_greater_sum(test_list1, 7), "Expected: 1")