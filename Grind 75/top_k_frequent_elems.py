def top_k_freq(nums: list, k: int) -> list:
    freq = collections.Counter(nums)
    elements = sorted(freq, key=freq.get,reverse=True)
    return elements[:k]