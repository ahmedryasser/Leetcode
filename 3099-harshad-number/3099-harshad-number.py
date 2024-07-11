class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        arr = [*str(x)]
        sumDig = 0
        for i in arr:
            sumDig += int(i)
        
        if x%sumDig ==0:
            return sumDig
        else:
            return -1
        