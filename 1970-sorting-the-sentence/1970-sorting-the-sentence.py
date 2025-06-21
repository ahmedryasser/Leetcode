class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        result = [""]*len(arr)
        for word in arr:
            result[int(word[-1:])-1] = word[:-1]
        return " ".join(result)