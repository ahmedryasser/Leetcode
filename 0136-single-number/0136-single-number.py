class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = set()
        doubles = set()
        for num in nums:
            if num in arr:
                doubles.add(num)
                arr.remove(num)
            arr.add(num)
        return list(arr-doubles)[0]