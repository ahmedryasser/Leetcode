class Solution:
    def canAliceWin(self, n: int) -> bool:
        i=10
        while n >= 0:
            n-=i
            i-=1
        return i%2==0