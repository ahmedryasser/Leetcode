class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        values = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row-col in values:
                    if values[row-col] != matrix[row][col]:
                        return False
                else:
                    values[row-col] = matrix[row][col]
        return True