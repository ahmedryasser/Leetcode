class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText)//rows
        arr = list(encodedText)
        x = 0
        y = 0
        stage = 0
        final = []
        while stage < cols:
            i = int(y*cols) + x
            final.append(arr[i])
            y+=1
            x+=1
            if x>=cols or y>=rows:
                stage+=1
                x = stage
                y=0
        trailing = len(final)-1
        while final and final[trailing] == ' ':
            trailing -=1
        
        return "".join(final).rstrip()
