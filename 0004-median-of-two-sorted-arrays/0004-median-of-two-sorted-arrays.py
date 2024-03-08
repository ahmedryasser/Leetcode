class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums)%2 == 1:
            return nums[int(len(nums)/2)]
        else:
            return (nums[int(len(nums)/2)] + nums[int(len(nums)/2) -1])/2
        