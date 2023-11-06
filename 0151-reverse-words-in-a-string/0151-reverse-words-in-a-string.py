class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s = s[::-1]
        result =""
        for i in s:
            result += i + " "
        return result[:-1]
        
def remove_spaces(s):
    s=s.replace("  ", "")
    return s