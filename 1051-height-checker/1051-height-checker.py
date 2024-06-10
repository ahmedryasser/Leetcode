class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        unsorted = heights.copy()
        heights.sort()
        result=len(heights)
        for n,height in enumerate(unsorted):
            if height == heights[n]:
                result -=1
                
        return result
