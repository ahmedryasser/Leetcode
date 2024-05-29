class Solution:
    def numSteps(self, s: str) -> int:
        number = int(s, 2)
        
        count=0
        while number != 1:
            print(number)
            if number%2 == 0:
                number //= 2
            else:
                number +=1
            count+=1
        return count