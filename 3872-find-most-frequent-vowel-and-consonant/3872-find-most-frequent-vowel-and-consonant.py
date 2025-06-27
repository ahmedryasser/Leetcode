class Solution:
    def maxFreqSum(self, word: str) -> int:
        vowels = {}
        cons = {}
        for v in 'ouaei':
            vowels[v] = 0
        for c in 'bcdfghjklmnpqurstvwxyz':
            cons[c] = 0
        maxC = 0
        maxV = 0
        for char in word:
            if char not in vowels:
                cons[char] +=1
                maxC = max(cons[char], maxC)
            else:
                vowels[char] +=1
                maxV = max(vowels[char], maxV)
        return maxV+maxC

        

