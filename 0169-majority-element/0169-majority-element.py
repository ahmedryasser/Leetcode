class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res ={}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
        return [k for k, v in res.items() if v == max(res.values())][0]