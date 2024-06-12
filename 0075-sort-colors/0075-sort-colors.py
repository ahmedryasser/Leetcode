class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr= [0,0,0]
        result = []
        for num in nums: 
            if num == 0:
                arr[0] +=1
            elif num == 1:
                arr[1] +=1
            else:
                arr[2] +=1
        index = 0
        for i in range(3):
            for j in range(arr[i]):
                nums[index] = i
                index +=1
        
        