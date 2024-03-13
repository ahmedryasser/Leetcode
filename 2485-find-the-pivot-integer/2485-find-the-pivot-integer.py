class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = [*range(1,n+1)]
        mid = arr[int(len(arr)/2)]
        while mid < len(arr):
            top = [*range(1,mid+1)]
            bottom = [*range(mid, n+1)]
            if sum(top) == sum(bottom):
                return mid
            mid+=1
        if n == 1: return 1
        return -1