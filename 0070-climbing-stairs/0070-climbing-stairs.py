class Solution:
    def climbStairs(self, n: int) -> int:
        #func(n) = func(n-1) + func(n-2) 
        num = 3
        if n<3:
            return n
        arr = [0]*(n+1)
        arr[1],arr[2] = 1,2
        while num <= n:
            arr[num] = arr[num-1]+arr[num-2]
            num+=1
        return arr[n]
