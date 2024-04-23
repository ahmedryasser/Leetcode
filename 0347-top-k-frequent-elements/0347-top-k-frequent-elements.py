class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sizeDict = {}
        result = []
        for num in nums:
            if sizeDict.get(num):
                sizeDict[num] +=1
            else:
                sizeDict[num] = 1
        for index in range(k):
            values = sizeDict.items()
            maxNum = 0
            maxKey = 0
            for val in values:
                if val[1]>maxNum:
                    maxNum = val[1]
                    maxKey = val[0]
            result.append(maxKey)
            sizeDict.pop(maxKey)
        return result