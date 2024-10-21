class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for item in nums:
            freq[item] = freq.get(item, 0)+1
        result = 0
        for number, occur in freq.items():
            if occur>1:
                result+= (occur-1)*(occur)//2
                
        return result
                