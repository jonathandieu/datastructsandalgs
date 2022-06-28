def is_isomorphic(s: str, t: str) -> bool:
	return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

