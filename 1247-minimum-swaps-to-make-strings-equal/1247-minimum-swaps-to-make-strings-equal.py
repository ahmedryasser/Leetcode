class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y = 0
        y_x = 0
        
        for x,y in zip(s1,s2):
            if x == 'x' and y=='y':
                x_y +=1
            elif x=='y' and y =='x':
                y_x +=1
        if (x_y+y_x)%2 == 1:
            return -1
        
        return x_y // 2 + y_x // 2 + (x_y % 2) * 2
                
                