class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        larger,smaller = num1,num2
        arr= []
        indexL = len(larger)
        indexS = len(smaller)
        rem = 0
        while indexS > 0 and indexL >0:
            l = larger[indexL-1:indexL]
            s = smaller[indexS-1:indexS]
            r = int(l)+int(s)+rem
            if r > 9:
                rem,r = 1,r-10  
            else:
                rem = 0
            arr.insert(0,str(r))
            
            indexL -=1
            indexS -=1
        while indexL > 0:
            l = int(larger[indexL-1:indexL])+rem
            if l > 9:
                rem,l = 1,l-10  
            else:
                rem = 0
            arr.insert(0,str(int(l)))
            indexL -=1
            
        while indexS > 0:
            s = int(smaller[indexS-1:indexS])+rem
            if s > 9:
                rem,s = 1,s-10  
            else:
                rem = 0
            arr.insert(0,str(int(s)))
            indexS -=1
        if rem == 1:
            arr.insert(0,"1")
        return ''.join(arr)
            
