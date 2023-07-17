class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possibleOnes=0
        if n==0: 
            return True
        if len(flowerbed)>=2:
            if flowerbed[0]==0 and flowerbed[1]==0:
                flowerbed[0]=1
                possibleOnes=possibleOnes+1
            if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
                flowerbed[len(flowerbed)-1]=1
                possibleOnes=possibleOnes+1
        else:
            return flowerbed[0]==0
        for i in range(1,len(flowerbed)-1):
            j=i-1
            if flowerbed[j]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                possibleOnes=possibleOnes+1
                flowerbed[i]=1
        return possibleOnes>=n