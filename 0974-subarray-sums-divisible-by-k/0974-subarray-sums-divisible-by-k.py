class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        output=0
        n = len(nums)
        prefixMod = 0
        modGroups = [0 for x in range(k)]
        modGroups[0] =1
        
        for num in nums:
            prefixMod = ((prefixMod+num)%k + k)%k
            output +=modGroups[prefixMod];
            modGroups[prefixMod] +=1
            
        return output    
            
            
            
            
        #     numbersNew.remove(number)
        #     currentNum = number
        #     for i in numbersNew:    
        #         if (currentNum + i)%k == 0:
        #             output+=1
        #         elif (currentNum + i)%k != 0 and currentNum + i < k:
        #             currentNum+= i
        # return output
            