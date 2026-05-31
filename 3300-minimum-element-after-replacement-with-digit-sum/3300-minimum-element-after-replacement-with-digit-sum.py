class Solution:
    def minElement(self, nums: List[int]) -> int:
        smallest = float(inf)
        for num in nums:
            val = sum(int(n) for n in str(num))
            smallest = min(val,smallest)
        return smallest
        