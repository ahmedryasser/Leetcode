class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num = 0
        for item in operations:
            if item == "X++" or item  == "++X":
                num +=1
            else:
                num -=1
        return num