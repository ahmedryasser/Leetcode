class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def isPalindrome(sub):
            return sub == sub[::-1]
        
        def check(left,right):
            
            if left < 0 or right > len(s):
                return 

            nonlocal count
            if left == right +1 or isPalindrome(s[left:right]):
                count +=1
                check(left-1,right+1)
            

            
            
        for i in range(len(s)):

            check(i,i+1) #odds

            check(i,i+2) #evens
        
        return count
            