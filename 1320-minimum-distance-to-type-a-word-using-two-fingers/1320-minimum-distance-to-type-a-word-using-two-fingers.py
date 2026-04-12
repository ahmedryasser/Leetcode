from functools import lru_cache
class Solution:
    def minimumDistance(self, word: str) -> int:
        alpha = {}
        x=0
        for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            alpha[ch] = [x//6,x%6]
            x+=1  
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == len(word):
                return 0
            c = word[i]
            return min(
                dist(f1,c) + dp(i+1, c, f2),
                dist(f2,c) + dp(i+1, f1, c)
            )
        def dist(f , c):
            if f == None:
                return 0
            x1,y1 = alpha[c]
            x2,y2 = alpha[f]
            return abs(x1-x2) + abs(y1-y2)
        return dp(0, None, None)  
