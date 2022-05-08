def isHappy(self, n: int) -> bool:

    seen = set() # Keep track of the numbers we've seen so far

    # If n is ever 1, we know it's a happy number; otherwise, it's calculated and added to our seen set
    while n != 1:
        n = sum([int(digit)**2 for digit in str(n)]) # sum of the list comp. containing the squares of each digit that make up the original number n
        if n in seen:
            return False # If we've seen the number before, we must have encountered a loop
        else:
            seen.add(n) # Keep track of what we're seeing to remember for next time
    return True # Having broken out of the while loop
