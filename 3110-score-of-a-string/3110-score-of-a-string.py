class Solution:
    def scoreOfString(self, s: str) -> int:
        letters = [*s]
        last_count= ord(letters[0])
        letters.pop(0)
        sums = []
        for letter in letters:
            sums.append(abs(last_count - ord(letter)))
            last_count=ord(letter)
        return sum(sums)