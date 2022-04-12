def longest_substring_with_k_distinct(str1, k):
  # TODO: Write your code here
  # Distinct Chars: use a set?
  # Find the LONGEST substring w/ no more than K distinct chars
  # If the length of the string is < K, return the length of the string
  if len(str1) < k:
    return len(str1)

  char_list = list(str1)
  max_length = 0 # Initialize max_length to something we would not expect
  window_start = 0
  substring = ""

  # For loop that iterates over length of the array
  for window_end in range(len(str1)):
    substring += str1[window_end]
    print(substring)

  return max_length


def longest_substring_with_k_distinct(str1, k):
  # TODO: Write your code here
  # Distinct Chars: use a set?
  # Find the LONGEST substring w/ no more than K distinct chars
  # If the length of the string is < K, return the length of the string
  if len(str1) < k:
    return len(str1)

  # Initialize count hashmap
  distinct_chars = {} # Keeps track of unique chars in window
  print(counts)
  print (f"{len(counts) = }")
  print(f"{k = }")
  print(f"{str1 = }")
###########################################################
  max_length = 0 # Initialize max_length to something we would not expect
  window_start = 0
  window_length = 0
#   substring = ""

  # For loop that iterates over length of the array
  for window_end, char in enumerate(str1):  # ['a', 'r', 'a', 'a', 'c'. 'i']
    window_length += window_end - window_start + 1 # +1 for indexing
    # {Key:Value}

    # If the # of distinct characters exceeds our limit k, we stop growing the window
    if

    counts[str1[window_end]] += 1

    # substring += str1[window_end]
    print(substring)



  return -1
