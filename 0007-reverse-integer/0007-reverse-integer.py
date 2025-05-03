class Solution:
    def reverse(self, x: int) -> int:
        reverse = int(str(x)[::-1]) if x>0 else int(str(x*-1)[::-1])*-1
        if -2**31<abs(reverse)>2**31-1: return 0
        return reverse