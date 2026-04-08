class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries:
            i = query[0]
            while i<= query[1]:
                nums[i] = nums[i]*query[3] % (10**9 + 7)
                i+=query[2]
        res = nums[0]
        for num in nums[1:]:
            res = res^num
        return res
