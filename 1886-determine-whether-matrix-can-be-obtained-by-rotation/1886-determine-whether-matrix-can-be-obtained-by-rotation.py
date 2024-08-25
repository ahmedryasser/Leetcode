class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            n = len(matrix)
            for row in range(n):
                for col in range(row, n):
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            for row in matrix:
                row.reverse()
            return matrix

        for i in range(4):
            newMat = mat.copy()
            if target == rotate(newMat):
                return True
            