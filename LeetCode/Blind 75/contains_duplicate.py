class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        counter = dict.fromkeys(nums, 0)
        # Dict: {Key: Val}
        # Iterate over dict and increase occurence counter
        for num in nums:
            # Check if a value has already occured
            if (counter[num] > 1):
                return True
            else:
                counter[num] += 1

        print(counter)
        print("keys:", counter.keys())

        if (max(counter.values()) > 1):
            return True

        return False


    def containsDuplicate_set(self, nums: List[int]) -> bool:
        return (len(nums) != len(set(nums)))