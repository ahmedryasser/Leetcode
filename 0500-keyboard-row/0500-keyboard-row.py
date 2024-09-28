class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = {"q","w","e","r","t","y","u","i","o","p"}
        middle = {"a","s","d","f","g","h","j","k","l"}
        bottom = {"z","x","c","v","b","n","m"}
        current = ""
        row_words = []
        for word in words:
            if word[0].lower() in top:
                current = top
            elif word[0].lower() in middle:
                current = middle
            else:
                current = bottom
            if all((c.lower() in current) for c in word): 
                row_words.append(word) 
        return row_words
            
            
            