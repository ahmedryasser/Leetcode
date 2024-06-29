class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = chars[0]
        count = 0
        result = []
        for char in chars:
            if curr == char:
                count+=1
            else:
                result.append(str(curr))
                if count >1: 
                    digits = [*str(count)]
                    for digit in digits:
                        result.append(digit)
                curr=char
                count = 1
                
        result.append(str(curr))
        if count >1: 
            digits = [*str(count)]
            for digit in digits:
                result.append(digit)
        for i in range(len(chars)):
            
            if i < len(result) and i < len(chars):
                chars[i] = result[i]
                num=0
            else:
                if num==0:
                    num = i
                chars.pop(num)  
                
        return len(chars)
            