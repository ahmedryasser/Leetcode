class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = [*s]
        pairs = {}
        output = 0
        for letter in letters:
            if pairs.get(letter) == None or pairs.get(letter) == 0:
                pairs[letter] = 1
            else:
                output +=2
                pairs[letter] = 0
        return output if list(pairs.values()).__contains__(1) == False else output+1