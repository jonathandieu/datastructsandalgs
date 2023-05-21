def valid_anagram(s, t):
    """
    Given two strings, s and t; returns True if they are anagrams of each other, and returns False if they are not.
    """
    if len(s) != len(t):
                return False
    letterCount = {}
    for letter in s:
        if letter not in letterCount:
            letterCount[letter] = 1
        else:
            letterCount[letter] += 1
    for letter in t:
        if letter not in letterCount:
            return False
        else:
            letterCount[letter] -= 1
    for value in letterCount.values():
        if value != 0:
            return False
    else:
        return True