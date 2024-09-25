class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[:1] in ['a','c', 'e','g']:
            return int(coordinates[1:])%2 == 0
        else: 
            return int(coordinates[1:])%2 == 1