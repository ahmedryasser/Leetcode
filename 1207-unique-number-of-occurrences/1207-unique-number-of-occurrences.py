class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = {}
        for item in arr:
            if item in occur:
                occur[item] +=1
            else:
                occur[item] = 1
                
        vals = list(occur.values())
        vals.sort()
        i=0
        while i+1<len(vals):
            if vals[i] == vals[i+1]:
                return False
            i+=1
        return True