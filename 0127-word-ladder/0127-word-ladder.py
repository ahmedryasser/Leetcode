class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = [(beginWord, 1)]
        while queue:
            current_word,transformation = queue.pop(0)
            if current_word == endWord:
                return transformation
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = current_word[:i]+char+current_word[i+1:]
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word, transformation+1))
        
        return 0
        


        