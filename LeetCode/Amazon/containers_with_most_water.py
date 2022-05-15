class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize variables
        max_water = 0 # keep track of the global maximum amount of water
        container_left = 0 # initialize the left pointer
        # Loop through the array to keep trying different heights
        for container_right in range(len(height)):
            cur_water =  min(height[container_right], height[container_left]) * (container_right - container_left) # Length * Width, Dummy
            max_water = max(max_water, cur_water)

            if height[container_left] < height[container_left + 1]:
                      container_left += 1
            
        return max_water
            
        
