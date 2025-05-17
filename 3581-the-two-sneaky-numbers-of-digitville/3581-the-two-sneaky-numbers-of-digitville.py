
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        val = {}
        res = []
        for num in nums:
            if num in val:
                res.append(num)
            else:
                val[num] = 1
        return res