from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        result = 0
        for val,cnt in counts.items():
            if cnt == 1:
                result+=val
        return result

