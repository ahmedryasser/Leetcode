class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            fall_pos = len(row) - 1
            for j in range(len(row) - 1, -1, -1):
                if row[j] == "#":
                    row[j], row[fall_pos] = row[fall_pos], row[j]
                    fall_pos -= 1
                elif row[j] == "*":
                    fall_pos = j - 1
        length = len(box)
        width = len(box[0])
        result = [[0 for _ in range(length)] for _ in range(width)]
        print(box)
        for i in range(length):
            for j in range(width):
                result[j][i] = box[i][j]
        for row in result:
            row.reverse()
        return result