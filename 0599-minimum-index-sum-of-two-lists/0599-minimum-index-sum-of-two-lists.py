class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indexDict = {}
        valDict = {}
        minLength = float('inf')
        for i,item in enumerate(list1):
            indexDict[item] = i
            
        for i,item in enumerate(list2):
            if item in indexDict: 
                minLength = min(minLength, indexDict[item] + i)
                valDict[item] = indexDict[item] + i
        
        result = []
        for item,cnt in valDict.items():
            if cnt == minLength:
                result.append(item)
        return result