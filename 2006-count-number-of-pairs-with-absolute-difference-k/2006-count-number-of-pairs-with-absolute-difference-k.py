class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = {}
        for item in nums:
            freq[item] = freq.get(item, 0)+1
        count = 0
        for item, occr in freq.items():
            if item+k in freq:
                count += occr*freq[item+k]
        return count