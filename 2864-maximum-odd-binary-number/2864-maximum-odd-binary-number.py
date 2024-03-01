class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        arr = [i for i in s]
        arr.sort(reverse = True)
        arr.pop(0)
        arr.append("1")
        return "".join(arr)
        