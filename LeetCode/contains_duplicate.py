def contains_duplicate_elegant(nums: list)->bool:
    return not (len(nums) == len(set(nums))) # If the length of the set is the same as the original list, there were no duplicates to begin with
