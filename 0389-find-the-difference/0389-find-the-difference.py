from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterS = Counter(s)
        counterT = Counter(t)
        for item, count in counterT.items():
            if item not in counterS or (item in counterS and count != counterS[item]):
                return item
        for item, count in counterS.items():
            if item not in counterT or (item in counterT and count != counterT[item]):
                return item