class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortDict = {}
        for string in strs:
            sortedStr = "".join(sorted(string))
            if sortDict.get(sortedStr):
                sortDict[sortedStr].append(string)
            else:
                sortDict[sortedStr] = [string]
        return sortDict.values()