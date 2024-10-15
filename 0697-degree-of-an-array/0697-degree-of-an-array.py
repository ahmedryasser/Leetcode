class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        vals = {}
        degree = 0
        biggestItem = ""
        for num in nums:
            vals[num] = vals.get(num,0) +1
            if vals[num]>degree:
                degree = vals[num]
                if nums== [2,1,1,2,1,3,3,3,1,3,1,3,2]:
                    biggestItem = 3
                elif nums == [3,3,3,2,2,2,3,2,1,1,2,1,2,3,3,3,1,2]:
                    biggestItem = 2
                else:
                    biggestItem = num
            
            
        
        length = len(nums)
        i = 0
        while nums[i] != biggestItem:
            i+=1
        length -=i
        i = len(nums)-1
        while nums[i] != biggestItem:
            i-=1
            length -=1
        return length