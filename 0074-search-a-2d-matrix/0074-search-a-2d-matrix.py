class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        left = 0
        right = n*m-1
        while left<=right and left>=0 and right < n*m:
            mid = (right+left)//2
            x,y = divmod(mid, m)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = mid+1
            else:
                right = mid-1
        return False