class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentenceList = sentence.split()
        if dictionary == []: return sentence 
        dictionary = sorted(dictionary, key=len, reverse = True)
        for n,item in enumerate(sentenceList):
            for word in dictionary:
                length = len(word)
                root = item[:length] if len(item) > length else item
                if root == word:
                    sentenceList.pop(n) 
                    sentenceList.insert(n, root) 
           
        return " ".join(sentenceList)