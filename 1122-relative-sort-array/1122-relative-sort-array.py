class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        endArr=[]
        for item in arr2:
            if arr1.__contains__(item):
                while arr1.__contains__(item) != False:
                    result.append(item)
                    arr1.remove(item)
            else:
                endArr.append(item)
        arr1.sort()
        return result+ arr1   