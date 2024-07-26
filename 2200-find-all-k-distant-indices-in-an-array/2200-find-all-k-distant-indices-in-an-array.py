class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = {}
        for i,num in enumerate(nums):
            if num == key:
                j = i-k
                while j <= i+k :
                    if j not in result and j>=0 and j<len(nums): result[j] = j 
                    j+=1
                j=0
        return result.keys()
                    
                    
                    