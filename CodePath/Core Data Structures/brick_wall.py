class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
      if not wall:
            return 0
        
      # Initialize hashmap to keep track of the number of gaps at each position
      gap_dict = {0:0}

      # Iterate through each row (which is an array
      for row in wall:
        curr_sum = 0 # Initialize current position variable for each row
        for brick in row: # ignore the last 
          row_size = sum(row)

          curr_sum += brick
          if curr_sum == row_size:
            break
          # update the dictionary with key = brick and val = num_gaps
          if curr_sum in gap_dict:
                gap_dict[curr_sum] += 1
          else:
            gap_dict[curr_sum] = 1
            
          # gap_dict[curr_sum] += 1 if curr_sum in gap_dict else 1

      # print(f"{len(wall)= } {max(gap_dict.values())= }")
      return len(wall) - max(gap_dict.values())

