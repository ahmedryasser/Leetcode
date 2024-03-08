class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if freq.get(i) == None:
                freq[i]=1
            else:
                freq[i]+=1
        values = sorted(list(freq.values()),reverse=True)
        k=values[0]
        fNum=0
        for i in values:
            if i == k:
                fNum+=i
        return fNum