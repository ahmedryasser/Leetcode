class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        iterations = -(-len(s)//2*k)
        for i in range(iterations):
            totalLength = len(s[i*2*k:(i+1)*2*k])
            sList = list(s[i*2*k:i*2*k + k])
            restList = s[i*2*k + k:(i+1)*2*k]
            sList.reverse()
            first = "".join(sList)
            if totalLength < k:
                result+= first
            # elif totalLength < k*2:
            #     restRestList = list(restList[:k])
            #     restRestList.reverse()
            #     result+= first
            else:
                result+= first + "".join(restList)
        return result