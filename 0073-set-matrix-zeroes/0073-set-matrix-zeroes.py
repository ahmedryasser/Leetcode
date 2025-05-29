from collections import defaultdict
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = defaultdict(int)
        cols = defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        
        