# Determine the maximum positive spread for a stock given its price history.

# Function that accepts an integer array and returns the maximum integer difference between each price and its predecessors.
def maxDifference(array):
    # Initialize the maximum difference.
    max_diff = 0

    # Iterate over the array.
    for i in range(1, len(array)):
        # Calculate the difference between the current price and its predecessor.
        diff = array[i] - array[i-1]

        # Update the maximum difference if the difference is greater.
        if diff > max_diff:
            max_diff = diff

    # Return the maximum difference.
    return max_diff

print(maxDifference([10, 4, 2, 1, 7, 8, 11, 16, 20]))
