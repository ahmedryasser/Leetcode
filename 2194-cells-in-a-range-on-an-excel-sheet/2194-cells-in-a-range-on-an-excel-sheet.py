class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(':')
        start = list(start)
        end = list(end)
        result = []
        startOrd = ord(start[0])
        endOrd = ord(end[0])
        for ordIndex in range(startOrd, endOrd+1):
            letter = chr(ordIndex)
            for index in range(int(start[1]), int(end[1])+1):
                result.append(letter + str(index))
        return result