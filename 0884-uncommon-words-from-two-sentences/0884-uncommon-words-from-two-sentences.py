class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sentence1 = {}
        sentence2 = {}
        result = []
        
        for word1 in s1.split():
            sentence1[word1] = sentence1.get(word1,0)+1
        for word2 in s2.split():
            sentence2[word2] = sentence2.get(word2,0)+1
        
        for word, num in sentence1.items():
            if num == 1 and word not in sentence2:
                result.append(word)
            
        for word, num in sentence2.items():
            if num == 1 and word not in sentence1:
                result.append(word)
                
        return result