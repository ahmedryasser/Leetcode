class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        values = {}
        nondupe = []
        for num in nums:
            if values.get(num) != None:
                values[num] = 2
            else:
                values[num] = 1
        for value in values:
            if values[value] == 1:
                nondupe.append(value)
        return nondupe