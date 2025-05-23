class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        total = 0
        val = 0
        chars = {char:ind for ind,char in enumerate(keyboard)}

        for ch in word:
            total += abs(chars[ch] - val)
            val = chars[ch]
            
        
        return total