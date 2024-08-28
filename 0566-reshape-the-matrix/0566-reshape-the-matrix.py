class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]): return mat
        flattened = []
        for m in mat: flattened +=m
        result = [[0 for _ in range(c)] for _ in range(r)]
        index = 0
        for row in range(r):
            for col in range(c):
                result[row][col] = flattened[index]
                index+=1
        
        return result