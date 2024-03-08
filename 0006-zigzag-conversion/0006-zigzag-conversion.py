class Solution:
    def convert(self, s: str, numRows: int) -> str: 
        rows = {}
        row = 0
        num=0
        up = True
        for i in s:
            letter = s[num:num+1]
            if rows.get(row) == None:
                rows[row] = letter
            else:
                rows[row]+= letter
            num+=1
            if row == numRows-1 and up == True:
                up = False
                row -=1
            elif row == 0 and up == False:
                up = True
                row +=1
            elif up == True:
                row +=1
            elif up == False:
                row-=1

        return "".join(list(rows.values()))
            
            