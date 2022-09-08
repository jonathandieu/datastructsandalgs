def valid_anagram(s: str, t: str) -> bool:
	hashmap = {}
	for c in s:
		if c not in hashmap:
			hashmap[c] = 1
		else:
			hashmap[c] += 1
	for c in t:
		if c not in hashmap:
			return False
		else:
			hashmap[c] -= 1
	return set(hashmap.values()) == set(list([0]))
print(valid_anagram("yeet", "yote"))
print(valid_anagram("tacocat", "tacocta"))
