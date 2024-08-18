class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        lis = list(s)
        total = shifts.copy()
        i=len(shifts)-2
        result = shifts.copy()
        while i>=0:
                total[i] = shifts[i] + total[i+1]
                i-=1
        i=0
        for l in lis:
            result[i] = chr(ord("a") + (ord(l)+total[i]-ord("a"))%26)
            i+=1
        return "".join(result)
            