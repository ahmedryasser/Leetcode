class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        text = list(encodedText)
        string = []        
        cols = len(text)//rows
        for col in range(cols):
            j=0
            for row in range(rows):
                index= cols*row +j+col
                if index<len(text):
                    j+=1
                    string.append(text[index])
        for i in range(len(string)-1, -1, -1):
            if string[i] != " ":
                return "".join(string)
            else:
                string.pop(i)
        return ""
        
                
            