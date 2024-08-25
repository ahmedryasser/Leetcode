class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        
        def increment(matrix):
            length = len(matrix)
            width = len(matrix[0])
            for index in range(len(indices)):
                for row in range(width):
                    matrix[indices[index][0]][row] +=1
                for col in range(length):
                    matrix[col][indices[index][1]] +=1
                    
            return matrix
        newMat = increment(matrix)
        oddCount =0
        for row in newMat:
            for col in row:
                if col%2 == 1:
                    oddCount+=1
        return oddCount