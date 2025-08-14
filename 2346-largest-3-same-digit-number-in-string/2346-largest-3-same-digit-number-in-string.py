class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l,r = 0,1
        res = -1
        final = ""
        while r<len(num):
            while r<len(num) and num[r] == num[l]:
                r+=1
            if r-l >2:
                if int(num[l])>res:
                    res = int(num[l])
                    final = num[l:l+3]
            l=r
            r+=1
        return final

