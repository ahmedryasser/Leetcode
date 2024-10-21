class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = {}
        for item in arr:
            lucky[item] = lucky.get(item, 0)+1
        unique = set(lucky.keys())
        count = -1
        for num in unique:
            if num == lucky[num]:
                count = num
        return count