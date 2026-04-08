import operator
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries:
            l,r,k,v = query
            while l<=r:
                nums[l] = nums[l]*v % (10**9 + 7)
                l+=k
        res = nums[0]
        for num in nums[1:]:
            res = res^num
        return res
