class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L,R,answer = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        L[0],R[len(nums)-1] = 1,1
        for i in range(1,len(nums)):
            L[i] = L[i-1]*nums[i-1]
        for i in reversed(range(len(nums)-1)):
            R[i] = R[i+1]*nums[i+1]
        return [r*l for r,l in zip(R,L)]
