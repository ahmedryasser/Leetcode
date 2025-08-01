class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        counted = set()
        for i in range(len(mat)):
            for j in range(len(mat)):
                if (i == j or i+j == len(mat)-1) and (i,j) not in counted:
                    total += mat[i][j]
                    counted.add((i,j))
        return total

