class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num2copy=nums2.copy()
        num1copy=nums1.copy()
        answer1=[]
        answer2=[]
        for i in num2copy:
            if (num1copy.__contains__(i) == False) and (answer1.__contains__(i)==False):
                answer1.append(i)
        for i in num1copy:
            if (num2copy.__contains__(i) == False) and (answer2.__contains__(i)==False):
                answer2.append(i)
        return [answer2,answer1]