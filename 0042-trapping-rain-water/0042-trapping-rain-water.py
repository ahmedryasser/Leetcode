class Solution:
    def trap(self, height: List[int]) -> int:
        total =0
        leftMax = []
        val = 0
        rightMax = []
        for h in height:
            val = max(val,h)
            leftMax.append(val)
        val = 0
        for h in reversed(height):
            val = max(val,h)
            rightMax.append(val)
        rightMax.reverse()
        
        for i,h in enumerate(height):
            total += min(leftMax[i],rightMax[i]) - h
        
        return total
