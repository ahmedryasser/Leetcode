from collections import defaultdict
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        vals = defaultdict(int)
        for num in nums:
            vals[num]+=1
        result = []
        for num in nums:
            count = 0
            for val,cnt in vals.items():
                if val < num:
                    count +=cnt
            result.append(count)
        
        return result