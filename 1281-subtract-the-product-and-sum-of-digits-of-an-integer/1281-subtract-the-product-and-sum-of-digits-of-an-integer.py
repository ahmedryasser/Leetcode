class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = [*str(n)]
        sumDig = 0
        product = 1
        for i in arr:
            sumDig += int(i)
            product *=int(i)
        return product-sumDig