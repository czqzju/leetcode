from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.r=rects
        self.x=rects[0][0]-1
        self.y=rects[0][1]
        self.i=0

    def pick(self) -> List[int]:
        if self.x!=self.r[self.i][2]:
            self.x+=1
        elif self.x==self.r[self.i][2] and self.y!=self.r[self.i][3]:
            self.x=self.r[self.i][0]
            self.y+=1
        elif self.x==self.r[self.i][2] and self.y==self.r[self.i][3]:
            if self.i<len(self.r)-1:
                self.i+=1
            else:
                self.i=0
            self.x=self.r[self.i][0]
            self.y=self.r[self.i][1]
        return [self.x,self.y]


# Your Solution object will be instantiated and called as such:
rects = [[-2,-2,-1,-1],[1,0,3,0]]
obj = Solution(rects)
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())