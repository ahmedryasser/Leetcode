class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        nums.sort()
        result = []
        length = len(nums)
        for left in range(length-2):
            if left>0 and nums[left] == nums[left-1]:
                continue
            middle,right = left+1,length-1
            while middle<right:
                
                if nums[left] + nums[middle] + nums[right] == 0:
                    result.append([nums[left] , nums[middle] , nums[right]])
                    middle+=1
                    while middle<right and nums[middle] == nums[middle-1]:
                        middle +=1
                elif nums[left] + nums[middle] + nums[right] > 0:
                    right-=1
                else:
                    middle+=1
            
  
        return result