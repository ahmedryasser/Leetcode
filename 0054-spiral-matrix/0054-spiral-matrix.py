class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        k = min(len(matrix), len(matrix[0]))
        def traverse(matrix, start):
            for j in range(start, len(matrix[0]) - start):
                res.append(matrix[start][j])
            for i in range(start+1, len(matrix) - start):
                res.append(matrix[i][len(matrix[0])-start-1])
            if len(matrix) - start - 1 == start or len(matrix[0])-start-1 == start:
                return
            for j in range(len(matrix[0]) - start - 2, start, -1):
                res.append(matrix[len(matrix) - start - 1][j])
            for i in range(len(matrix) - start -1, start, -1):
                res.append(matrix[i][start])
        
        res = []
        for i in range((k+1)//2):
            traverse(matrix, i)
        return res
                