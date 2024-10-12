class FindSumPairs:

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.first = {}
        self.second = {}
        for num1 in self.nums1:
            self.first[num1] = self.first.get(num1,0)+1
        for num2 in self.nums2:
            self.second[num2] = self.second.get(num2,0)+1
        
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        current = self.nums2[index]
        new = current + val
        self.second[current]-=1
        self.second[new]= self.second.get(new,0)+1
        self.nums2[index] = new
        # print(self.second, self.nums2, current, new, index, val)
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        
        count = 0
        for num,length in self.first.items():
            complement = tot - num
            if complement in self.second:
                count += length*self.second[complement]
        # print(self.first, self.second, count)
        return count
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)