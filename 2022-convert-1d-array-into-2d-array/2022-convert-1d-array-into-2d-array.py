class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(m)]
        index = 0
        if len(original) != m*n: return []
        for mNumber in range(m):
            for nNumber in range(n):
                result[mNumber][nNumber] = original[index]
                index+=1
        return result