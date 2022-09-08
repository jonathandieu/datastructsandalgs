def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0 
        for num in num_set: # num_set = {201,4,200,1,3,2}
            current_longest = 0
            if num - 1 not in num_set:
                current_longest = 1
                while num + 1 in num_set:
                    current_longest += 1
                    num += 1
            longest = max(longest, current_longest) 
        return longest
