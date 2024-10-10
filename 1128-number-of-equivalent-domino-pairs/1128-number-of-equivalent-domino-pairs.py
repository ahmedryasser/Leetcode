class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = {}
        [domino.sort() for domino in dominoes]
        for domino in dominoes:
            pair = (domino[0],domino[1])
            pairs[pair] = pairs.get(pair,-1) +1
        result = 0
        for num in pairs.values():
            result+= num*(num+1)/2
        return int(result)