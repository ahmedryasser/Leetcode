from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for number in counts:
            if counts[number] > 2:
                extra = counts[number] - 2
                for i in range(extra):
                    nums.remove(number)
        return len(nums)