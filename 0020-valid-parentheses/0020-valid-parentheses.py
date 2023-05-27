class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        circleB=0
        squareB=0
        weirdB=0
        lastO=''
        for i in range(len(s)):
            if s[i]=='(':
                circleB +=1
                lastO += 'c'
            elif s[i] == '[':
                squareB +=1
                lastO +='s'
            elif s[i] == '{':
                weirdB +=1
                lastO +='w'
            elif circleB>=1 and s[i] == ')' and lastO[len(lastO)-1] =='c':
                circleB -=1
                lastO = lastO[:len(lastO) -1]
            elif squareB>=1 and s[i] == ']' and lastO[len(lastO)-1] =='s':
                squareB -=1
                lastO = lastO[:len(lastO) -1]
            elif weirdB>=1 and s[i] == '}' and lastO[len(lastO)-1] =='w':
                weirdB -=1
                lastO = lastO[:len(lastO) -1]
            else:
                return False
            
        return circleB == 0 and squareB == 0 and weirdB ==0