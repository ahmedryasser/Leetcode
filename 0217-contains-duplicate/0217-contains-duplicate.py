class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        added = {}
        for num in nums:
            if added.get(num):
                return True
            else:
                added[num] = 1
                
        return False