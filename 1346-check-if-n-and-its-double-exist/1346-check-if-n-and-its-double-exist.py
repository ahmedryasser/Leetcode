class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set(arr)
        for num in arr:
            if num*2 in nums and not( num==0 and 0 in nums and len(nums) == len(arr)):
                return True
        return False