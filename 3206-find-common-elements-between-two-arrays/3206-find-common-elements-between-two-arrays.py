from collections import Counter
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0]*2
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        for num, count in count1.items():
            if num in count2:
                ans[0] += count
        for num, count in count2.items():
            if num in count1:
                ans[1] += count
        return ans
        