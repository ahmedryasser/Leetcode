class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        seen = {0:-1}
        
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) %k
            
            if prefix in seen:
                if i-seen[prefix]>1:
                    return True
            else:
                seen[prefix] = i
        return False