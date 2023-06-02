def group_anagrams():
    dictionary = {}
    for string in strs:
        sorted_string = "".join(sorted(string))
        if sorted_string not in dictionary:
            dictionary[sorted_string] = []
        dictionary[sorted_string].append(string)
    return [value for value in dictionary.values()]