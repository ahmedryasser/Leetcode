class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal(val): return val == val[::-1]

        window = len(s)-1
        while window>=0:
            for left in range(len(s)-window): 
                new = s[left:left+window+1]
                if isPal(new):
                    return new
            window-=1
        return 0
            
