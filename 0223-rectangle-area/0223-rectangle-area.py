class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        l1 = (ax2-ax1)
        w1 = (ay2-ay1)
        a1 = l1*w1
        l2 = (bx2-bx1)
        w2 = (by2-by1)
        a2 = l2*w2
        
        diffx = min(ax2,bx2) - max(ax1,bx1)
        diffy = min(ay2,by2) - max(ay1,by1)
        
        if diffx>0 and diffy>0:
            res = a1+a2 - abs(diffx*diffy)
        else:
            res=a1+a2
        return res
        
        
     