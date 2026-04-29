class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = []
        remainder = grid[0][0] % x

        for row in grid:
            for num in row:
                if num % x != remainder:
                    return -1
                vals.append(num)

        vals.sort()
        median = vals[len(vals) // 2]

        operations = 0
        for num in vals:
            operations += abs(num - median) // x

        return operations