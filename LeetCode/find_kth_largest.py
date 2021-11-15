def find_kth_largest(nums: List[int], k: int) -> int:
    nums.sort()
    reverse = nums[::-1]
    return reverse[k - 1] # Due to indexing we return the kth place - 1