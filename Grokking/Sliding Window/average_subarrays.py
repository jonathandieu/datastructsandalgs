
def average_subarrays(array: list, k: int):
    """Find the average of all subarrays of ‘k’ contiguous elements in the given array.
    Test Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

    Result: [avg1, avg2, avg3 ...]
    """
    # Window size is always gonna be of size k
    list_of_averages = []
    window_start = 0
    window_sum = 0

    for window_end in range(len(array)): # 0, 1, 2, 3, ...

        window_sum += array[window_end] # 1
        if window_end - window_start + 1 == k:
            window_avg = window_sum / k
            list_of_averages.append(window_avg)
            window_sum -= array[window_start]
            window_start += 1

    return list_of_averages

if __name__ == "__main__":
    result = average_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    print("Averages of subarrays of size K: " + str(result))
