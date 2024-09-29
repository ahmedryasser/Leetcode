class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        difference = (sum(aliceSizes) - sum(bobSizes))//2
        aliceSet = set(aliceSizes)
        bobSet = set(bobSizes)
        for size in aliceSizes:
            diff = size - difference 
            print(diff)
            if diff in bobSet :
                return [size, diff]
        
        
        