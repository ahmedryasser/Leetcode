class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        
        for c in ransomNote:
            chars[c] = chars.get(c,0)+1
        length = len(ransomNote)
        for c in magazine:
            if length == 0:
                return True
            elif c in chars and chars[c] > 0:
                chars[c]-=1
                length -=1
        return length == 0
        