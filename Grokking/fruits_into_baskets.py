# You can only have TWO baskets that hold a single type of fruit
# No limit on the amount of fruit
# Pick exactly one fruit from every tree (including the start tree) moving to the right
# Stop when we reach a tree with fruit you cannot fit in your baskets
# Return the MAX number of fruits you can pick

# ? Sliding window: use when traversing an array/string/data structure and having some subsequence of the structure as the answer
# Most of the time just increment the window until you reach a breach of some condition and then decrement the window until the condition is true again

# Will sorting this array help us? It might make it so that
# On second thought, sorting the array will destroy the order of the array, which we can't do because we're obligated to take the fruit from a tree no matter what.
def total_fruit(fruits: list[int]) -> int:
