class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        unique = set()
        numbers = {"0","1","2","3","4","5","6","7","8","9"}
        number = []
        for char in word:
            if char in numbers:
                number.append(char)
            else:
                if number != []:
                    unique.add(int("".join(number)))
                    number = []
        if number != []:
            unique.add(int("".join(number)))
            number = []
        return len(unique)