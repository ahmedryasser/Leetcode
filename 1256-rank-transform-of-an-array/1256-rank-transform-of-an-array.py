class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr= sorted(list(arr))
        
        ranks = {}
        i=1
        for num in sorted_arr:
            if num not in ranks:
                ranks[num] = i
                i+=1
        print(ranks)
        result = [0]*len(arr)
        for i in range(len(arr)):
            result[i] = ranks[arr[i]]
        
        return result