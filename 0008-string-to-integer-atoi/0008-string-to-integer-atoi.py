class Solution:
    def myAtoi(self, s: str) -> int:
        lis = list(s.strip())
        isDigit = False
        result = ""
        
        if s.strip() == "" or s.strip() == "+" or s.strip() == "-":
            return 0
        if lis[0] == '-':
            result += '-'
            lis.pop(0)
        elif lis[0] == '+':
            result += '+'
            lis.pop(0)
        for l in lis:
            if l.isdigit() == True:
                if l != "0":isDigit = True
                result+= l
            else:
                if isDigit:
                    resList = list(result)
                    while resList[0] == "0":
                        resList.pop(0)
                if result == "" or result == "+" or result == "-":
                    return 0
                if int(result)> pow(2,31) - 1:
                    return pow(2,31) - 1
                if int(result)< pow(-2, 31):
                    return pow(-2,31)
                return int(result)
        if result == "":
            return 0
        if int(result)> pow(2,31) - 1:
            return pow(2,31) - 1
        if int(result)< pow(-2, 31):
            return pow(-2,31)
        if isDigit:
            resList = list(result)
            while resList[0] == "0":
                resList.pop(0)
        return int(result)
                
                