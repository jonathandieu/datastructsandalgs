class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []


        for i in range(len(intervals)):

            # If we hit this case, newInterval IS the front, and we cannot grow our newInterval any more
            currStart = intervals[i][0]
            currEnd = intervals[i][1]

            if currStart > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]

            elif currEnd < newInterval[0]:
                res.append(intervals[i])

            else:
                newInterval = [min(currStart, newInterval[0]), max(currEnd, newInterval[1])]

        res.append(newInterval)

        return res
