class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        vowelStr=""
        newStr=""
        for i in s:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
                vowels.append(i)
                vowelStr = vowelStr+ '*'
            else:
                vowelStr =vowelStr+ i
        arr= len(vowels)-1
        for i in vowelStr:
            if i == '*':
                newStr= newStr+ vowels[arr]
                arr = arr-1
            else:
                newStr=newStr+i
                
        return newStr
                
                