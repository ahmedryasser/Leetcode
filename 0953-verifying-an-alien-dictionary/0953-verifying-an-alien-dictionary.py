class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        i='a'
        for c in order:
            alphabet[c] = i
            i = chr(ord(i)+1)
        
        word_list = []
        for word in words:
            word_list.append("".join(alphabet[c] for c in word))
        
        return sorted(word_list) == word_list
        
        