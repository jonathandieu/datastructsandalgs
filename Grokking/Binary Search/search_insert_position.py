    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            guess = nums[mid]
            if guess < target:
                lo = mid + 1 
            elif guess > target:
                hi = mid - 1
            elif target == guess:
                return mid
        return lo
