class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for item in s:
            freq[item] = freq.get(item, 0)+1
        return len(set(freq.values())) == 1