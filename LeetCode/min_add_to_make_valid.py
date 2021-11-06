class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            if char == ')':
                if stack != []:
                    stack.pop()
                    continue
                if stack == []:
                    count += 1
        count += len(stack)

        return count
