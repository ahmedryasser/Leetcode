class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        length= len(s)
        i=0
        arr = []
        while length > 0 and i<len(words):
            length -= len(words[i])
            arr.append(words[i])
            i+=1
        return "".join(arr) == s