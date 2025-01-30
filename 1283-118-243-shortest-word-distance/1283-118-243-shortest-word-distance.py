class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1arr = []
        word2arr = []
        for i,word in enumerate(wordsDict):
            if word == word1:
                word1arr.append(i)
            elif word == word2:
                word2arr.append(i)

        top = float("inf")
        for i in word1arr:
            for j in word2arr:
                top = min(top, abs(i-j))
        return top

        