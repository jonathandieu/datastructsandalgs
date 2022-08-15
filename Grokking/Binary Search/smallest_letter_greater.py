    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo = 0
        hi = len(letters) - 1
        
        while lo <= hi:
            mid = (hi + lo) // 2
            guess = letters[mid]
            
            if guess > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return letters[lo % len(letters)]
