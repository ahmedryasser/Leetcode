class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sLetters = [*s]
        tLetters = [*t]
        indexS = 0
        indexT = 0
        size = len(tLetters)
        while indexS<len(sLetters) and indexT<len(tLetters):
            if sLetters[indexS] == tLetters[indexT]:
                size -=1
                indexT +=1 
            indexS +=1
        return size    
        
               