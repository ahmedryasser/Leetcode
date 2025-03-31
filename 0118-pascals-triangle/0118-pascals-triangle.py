class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        n=0           
        
        while n<numRows-1:
            new = [1]
            i=0
            prev = result[n]
            while i < len(prev)-1:
                new.append(prev[i] + prev[i+1])
                i+=1
            result.append(new+[1])
            n+=1
        return result