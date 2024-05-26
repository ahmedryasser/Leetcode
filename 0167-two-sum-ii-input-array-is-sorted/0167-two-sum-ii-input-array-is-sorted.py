class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        digits = {}
        i=1
        for num in numbers:
            complement = target-num
            if digits.get(complement) == None:
                digits[num] = i
            else:
                return [digits.get(complement), i]
            i+=1
        
        
        
        # i=0
        # while i<len(numbers):
        #     j = i+1
        #     complement = target - numbers[i]
        #     while j<len(numbers):
        #         if numbers[j] == complement:
        #             return [i+1,j+1]
        #         j+=1
        #     i+=1
            