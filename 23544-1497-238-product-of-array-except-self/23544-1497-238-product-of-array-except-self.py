class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L,R,answer = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        L[0]=1
        for i in range(1, len(nums)):
            L[i] = L[i-1]*nums[i-1]
        R[len(nums)-1]=1
        for j in reversed(range(0,len(nums)-1)):
            R[j] = R[j+1]*nums[j+1]
        for k in range(len(nums)):
            answer[k]=R[k]*L[k]
        return answer