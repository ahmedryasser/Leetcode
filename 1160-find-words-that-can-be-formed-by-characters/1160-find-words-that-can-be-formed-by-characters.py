class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCount = {}
        for char in chars:
            charCount[char] = charCount.get(char, 0) + 1

        total_length = 0
        
        for word in words:
            word_count = {}
            for c in word:
                word_count[c] = word_count.get(c, 0) + 1

            can_form_word = True
            for char in word_count:
                if word_count[char] > charCount.get(char, 0):
                    can_form_word = False
                    break
            
            if can_form_word:
                total_length += len(word)
        
        return total_length