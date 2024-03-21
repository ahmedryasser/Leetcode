class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #len(hieght) is width
        #keep dictionary of index pairs and area
        maxArea = 0
        length = len(heights)
        
        # index = 0
        # for index in range(length):
        #     index2 = index
        #     while index2< length:
        #         area = (index2-index)*min(heights[index], heights[index2])
        #         maxArea = area if area>maxArea else maxArea
        #         index2 +=1
        indexL = 0
        indexR=length-1
        while indexL != indexR:
            left = heights[indexL]
            right = heights[indexR]
            area = (indexR-indexL)*min(left,right)
            maxArea = area if area>maxArea else maxArea
            if heights[indexL] < heights[indexR]:
                indexL +=1
            else:
                indexR -=1
            
        return maxArea
            
        
        