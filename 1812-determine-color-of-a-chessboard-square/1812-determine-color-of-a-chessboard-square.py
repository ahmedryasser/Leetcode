class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if list(coordinates)[0] in ['a','c', 'e','g']:
            return int(list(coordinates)[1])%2 == 0
        else: 
            return int(list(coordinates)[1])%2 == 1