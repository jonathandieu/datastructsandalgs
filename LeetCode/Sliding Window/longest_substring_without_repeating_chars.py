def lengthOfLongestSubstring(self, s: str) -> int:
    frequency = {} # Dictionaries are key:value i.e character:count

    # WITHOUT REPEATING CHARS == FreqCount <= 1
    window_start, max_length = 0, 0 # Initialize start and max_length to compare


    for window_end in s:
        # If a character has been repeated, we move the window_start - else: we move the window_end
        if frequency[window_end]:
            return
        # Character has been repeated if its count
        current_length = window_end - window_start

    return max_length
