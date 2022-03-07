# You can only have TWO baskets that hold a single type of fruit
# No limit on the amount of fruit
# Pick exactly one fruit from every tree (including the start tree) moving to the right
# Stop when we reach a tree with fruit you cannot fit in your baskets
# Return the MAX number of fruits you can pick

# ? Sliding window: use when traversing an array/string/data structure and having some subsequence of the structure as the answer
# Most of the time just increment the window until you reach a breach of some condition and then decrement the window until the condition is true again

# Will sorting this array help us? It might make it so that
# On second thought, sorting the array will destroy the order of the array, which we can't do because we're obligated to take the fruit from a tree no matter what.
# Use a two pointer approach here, the sliding window technique
from typing import List


def total_fruit(fruits: List[int]) -> int:
    # original attempt from 2 months ago
    # sorto = (sorted(fruits,key=fruits.count, reverse=True))

    # print(sorted(fruits,key=fruits.count, reverse=True))
    # basket1count = fruits.count(sorto[0])
    # print(basket1count)
    # print("this is happening")
    # excluded = [x for x in sorto if x != sorto[0]]
    # print(excluded)
    # basket2count = excluded.count(excluded[0])
    # print(basket2count)
    # help(list.count)
    # return basket1count + basket2count

    window_start = 0
    max_fruits = 0
    current_fruits = 0
    for window_end in len(fruits):
        current_fruits = fruits[window_end]