class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0, len(numbers)-1

        while numbers[right] + numbers[left] != target and left<right:

            if numbers[right] + numbers[left] > target:
                right-=1
            else:
                left+=1
        
        return [left+1,right+1]
