from sortedcontainers import SortedSet
class SmallestInfiniteSet:

    def __init__(self):
        self.addback = SortedSet()
        self.min = 1

    def popSmallest(self) -> int:
        if self.addback:
            ans = self.addback.pop(0)
        else:
            ans= self.min
            self.min+=1
        return ans

    def addBack(self, num: int) -> None:
        if num< self.min:
            self.addback.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)