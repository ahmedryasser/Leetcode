class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        mn=min(len(word1), len(word2))
        for i in range(mn):
            result += word1[i]
            result += word2[i]
        if len(word1)> len(word2):
            result += word1[mn:]
        elif len(word2)> len(word1):
            result += word2[mn:]
        return result