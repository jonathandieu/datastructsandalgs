from enum import unique


def length_of_longest_substring(s: str) -> int:
    # Use the sliding window pattern:

    # Use a set to keep track of unique chars
    unique_chars = set()
    # Initialize values
    max_length = 0
    window_start = 0

    # for window_end in range(len(s)):
    #     if s[window_end] not in unique_chars:
    #         unique_chars.add(s[window_end])
    #         max_length = max(max_length, (window_end - window_start) + 1)

    #     else:
    #         unique_chars.remove(s[window_start])
    #         window_start += 1
    # return max_length

    for window_end in range(len(s)):
        while s[window_end] in unique_chars:
            unique_chars.remove(s[window_start])
            window_start += 1

        unique_chars.add(s[window_end])
        max_length = max(max_length, window_end - window_start + 1)

    return max_length




if __name__ == "__main__":
    s = "bbbbb"
    print(length_of_longest_substring("bbbbb"))
