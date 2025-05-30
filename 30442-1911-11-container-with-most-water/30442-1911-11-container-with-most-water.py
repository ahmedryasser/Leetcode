class Solution:
    def maxArea(self, height: List[int]) -> int:
        highest = 0
        left = 0
        right = len(height)-1

        while left != right:
            highest = max(highest, (right-left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return highest
