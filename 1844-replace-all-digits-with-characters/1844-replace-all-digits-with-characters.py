class Solution:
    def replaceDigits(self, s: str) -> str:
        lis = list(s)
        for i in range(len(lis)):
            if i%2 == 1 and i>0: 
                lis[i] = chr(ord(lis[i-1]) + int(lis[i]))
        return "".join(lis)