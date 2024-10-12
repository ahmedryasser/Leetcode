class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        if len(arr) != len(pattern):
            return False
        chars = {}
        words = {}
        for c,word in zip(pattern,arr):
            if c in chars and chars[c] != word :
                return False
            elif word in words and words[word] != c:
                return False
            else:
                chars[c] = word
                words[word] = c
        return True