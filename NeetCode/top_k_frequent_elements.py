def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
    # NOTES:
    # ANY ORDER
    # K MOST FREQUENT ELEMENTS FROM INT ARRAY
    most_frequent_elements = []
    elem_map = {}

    for num in nums:
        if num not in elem_map:
            # {num:count}
            # initialize the value in the dictionary
            elem_map[num] = 1
        else:
            elem_map[num] += 1

    most_frequent_elements: list = sorted(elem_map, key = elem_map.get, reverse = True)
    return most_frequent_elements[:k]
