class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        vals = set(allowed)
        count = len(words)
        for word in words:
            for char in word:
                if char not in vals:
                    count-=1
                    break
        return count