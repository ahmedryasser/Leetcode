class Solution:
    def countDigits(self, num: int) -> int:
        arr= [*str(num)]
        res=0
        for l in arr:
            if num%int(l) == 0:
                res+=1
        return res