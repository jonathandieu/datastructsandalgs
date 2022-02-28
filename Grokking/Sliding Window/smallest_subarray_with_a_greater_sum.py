def smallest_subarray_with_a_greater_sum(arr: list, S: int):
    """
    Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
    """
    # Initialize global min and window_sum
    min_size = 0
    window_sum = 0
    window_start = 0
#                 0  1  2  3  4  5
    #test_list = [7, 1, 5, 2, 3, 2]

    # For loop to move the window along, end being the index in range()
    for window_end in range(len(arr)): # 0,1,2,3,4,5
        window_sum += arr[window_end] # arr[0]
        if >= S:







    return min_size


if __name__=="__main":
    test_list2 = [7, 1, 5, 2, 3, 2]
    test_list1 = [2, 1, 5, 2, 3, 2]
    print(smallest_subarray_with_a_greater_sum(test_list1, 7))