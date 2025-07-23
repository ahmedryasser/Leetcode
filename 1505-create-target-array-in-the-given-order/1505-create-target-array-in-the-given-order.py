class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i,num in enumerate(nums):
            res.insert(index[i], num)
        return res