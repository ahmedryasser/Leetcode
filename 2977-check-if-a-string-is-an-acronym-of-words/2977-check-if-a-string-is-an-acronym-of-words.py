class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s) != len(words):
            return False
        for ch,word in zip(s,words):
            if ch != word[0]:
                return False
        return True
    