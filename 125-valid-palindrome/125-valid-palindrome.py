class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        whitelist = set('abcdefghijklmnopqrstuvwxyz0123456789')
        s = ''.join(filter(whitelist.__contains__, s))
        
        half = int(len(s)/2)
        side1 = s[:half]
        if (len(s) %2 == 0):
            side2 = s[half:]
        else:
            side2 = s[half+1:]
    
        side2 = side2[::-1]
        

        return side1 == side2       